from mrjob.job import MRJob
from mrjob.step import MRStep
import re

REGEX_ONLY_WORDS = "[\w']+"

class MRDataMining(MRJob):

    def steps(self):
        return [
            MRStep(mapper = self.mapper_get_words, reducer = self.reducer_count_words),
            MRStep(reducer = self.reducer_find_max_word)
        ]

    def mapper_get_words(self, _, line):
        words = re.findall(REGEX_ONLY_WORDS, line)
        for word in words:
            yield word.lower(), 1

    def reducer_count_words(self, word, count):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        
        yield None, (sum(count), word)

    def reducer_find_max_word(self, _, count_words_pair):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
            yield max(count_words_pair)

if __name__ == '__main__':
    MRDataMining.run()
