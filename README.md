# PROJECT BUILDING A BIG DATA ECOSYSTEM IN THE AWS CLOUD

- Project developed during the Cognizant Cloud Data Engineer Bootcamp on the Digital Innovation One platform with the objective of extracting and counting words from a book in plain text format, displaying the most frequent word, through a python algorithm.

- The algorithm was developed using the MRJOB and MRSTEPS library to create mapreduce jobs. This code is responsible for creating the cluster in the Elastic MapReduce (EMR) service, using the concept of infrastructure as code, without the need to manually create the cluster through the AWS console. The EMR is responsible for processing the given book data (input data), storing the counted words (output data) in S3.

## Project steps

- Create a datalake (bucket) structure in the S3 datastore service

- Inside the bucket, create the folder structures below: data output temp
Create SSH key from EC2 console and download .pem file

- SSH keys are to allow remote access from my machine to the AWS system
Get AWS Secret Id and Key to Configure MrJob

- Create a python virtual environment on a linux virtual machine

- Create a python virtual environment
In the python virtual environment:

- Create dio-aws-mostcommon-word.py word parsing algorithm in VS CODE
Install boto3: pip install boto3
Install mrjob: pip install mrjob
Configure the .mrjob.conf file located in the /etc folder
Access S3 and Upload File to Bucket

- In the python virtual environment, run a command in the VM's linux terminal for python to run the algorithm and create the cluster in EMR, process the data and store the output data in S3 in the appropriate folders

Access EMR and verify the cluster created

Access S3 and check the generated data in the folders
