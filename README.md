# PROJETO CONSTRUÇÃO DE UM ECOSSISTEMA DE BIG DATA NA NUVEM AWS

Projeto desenvolvido durante o Bootcamp Cognizant Cloud Data Engineer na plataforma Digital Innovation One 
com o objetivo de extrair e contabilizar palavras de um livro no formato de texto plano, exibindo a palavra de maior frequência, por meio de um algoritmo python.

O algoritmo foi desenvolvido utilizando a biblioteca MRJOB e MRSTEPS para criar mapreduce jobs. Esse código é responsável por criar o cluster no 
serviço Elastic MapReduce (EMR), utilizando o conceito de infraestrutura como código, sem a necessidade de criar manualmente o cluster pelo console da AWS.
O EMR é responsável pelo processamento dos dados do livro fornecido (dados de entrada), armazenando as palavras contabilizadas (dados de saída) no S3.


## Etapas do projeto

* Criar uma estrutura de datalake (bucket) no serviço de armazenamento de dados S3
    * Dentro do bucket, criar as estruturas de pasta abaixo:
        _data_
        _output_
        _temp_
 
* Criar chave SSH pelo console do EC2 e fazer download do arquivo .pem
    * As chaves SSH são para permitir o acesso remoto da minha máquina ao sistema da AWS
  
* Obter Id e chave secreta AWS para configurar o MrJob
  
* Criar um ambiente virtual python em uma máquina virtual linux
   * Criar um ambiente virtual python

* No ambiente virtual python: 
   * Criar algoritmo de análise de palavras dio-aws-mostcommon-word.py no VS CODE
   * Instalar boto3: pip install boto3
   * Instalar mrjob: pip install mrjob
   * Configurar o arquivo .mrjob.conf localizado na pasta /etc

* Acessar o S3 e fazer o upload de arquivo para o bucket 

* No ambiente virtual python, rodar comando no terminal linux da VM para o python executar o algoritmo e fazer a criação do cluster no EMR, processar os dados e armazenar os dados de saída no S3 nas pastas apropriadas 
  
* Acessar EMR e verificar o cluster criado 
   
* Acessar o S3 e verificar os dados gerados nas pastas
