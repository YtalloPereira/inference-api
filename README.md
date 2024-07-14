# 🎥 Inference API

O projeto Inference API foi desenvolvido como parte das sprints 4 e 5 do programa de bolsas Compass UOL para formação em machine learning na AWS. Ele consiste em uma API que realiza inferência com um modelo de machine learning treinado com o framework XGBoost no Amazon SageMaker.

## 📖 Índice

- [📝 Descrição do projeto](#-inference-api)
- [⚙️ Tecnologias utilizadas](#️-tecnologias-utilizadas)
- [🏛️ Arquitetura](#️-arquitetura)
- [🚀 Execução e utilização](#-execução-e-utilização)
  - [Pré-requisitos](#pré-requisitos)
  - [Passos para execução local dos notebooks com o Jupyter Notebooks](#passos-para-execução-local-dos-notebooks-com-o-jupyter-notebooks)
  - [Passos para execução local da API com Python e Docker](#passos-para-execução-local-da-api-com-python-e-docker)
  - [Passos para o deploy com o EC2 e Docker](#passos-para-o-deploy-com-o-ec2-e-docker)
- [🧱 Estrutura do projeto](#-estrutura-do-projeto)
- [🚧 Desafios e soluções](#-desafios-e-soluções)
- [👥 Contribuidores](#-contribuidores)

## ⚙️ Tecnologias Utilizadas
- **Python** 
     - **Biblioteca boto3** que possibilita a integração com os serviços da aws utilizados
     - **FastAPI** para criação de um endpoint para cosulta ao modelo
     - **Numpy e pandas** para o tratamento de dados
- **AWS** 
     - **SageMaker** para o treinamento do modelo de aprendizagem
     - **RDS** para trabalhar as bases de dados
     - **EC2** para deploy da aplicação
     - **S3** para armazenar o modelo de aprendizado
- **Docker e Docker Compose** 
     - **criar imagem** do projeto e executá-lo localmente por linha de comando e arquivo de configuração
- **Jupyter Notebooks**
     - Para execução dos códigos da análise de dados

## 🏛️ Arquitetura
   ![Esquema mostrando a cloud aws com usuários acessando api gateway esta recebendo o modelo do bucket s3. Sagemaker ligado ao bucket para fornecer o modelo e ao RDS para ler e atualizar o dataset.](assets/sprint4-5.jpg)
## 🚀 Execução e Utilização

### Pré-requisitos

- **Git** *(clonar o repositório e visualizar o versionamento)*
- **Python** *(baixar as dependências necessárias e executar a api e os notebooks localmente)*
- **Docker** *(criar imagem do projeto e executá-lo localmente por linha de comando)*
- **Docker Compose** *(criar imagem do projeto e executar localmente por arquivo de configuração)*
- **Conta na AWS** *(fazer deploy da api no EC2, treinar o modelo no SageMaker, armazenar dataset no RDS, armazenar modelo no S3)*
- **AWS CLI** *(executar comandos via terminal para interagir com os serviços AWS igual o console da AWS)*

---

### Passos para execução local dos notebooks com o Jupyter Notebooks

Este guia fornece instruções passo a passo para configurar e fazer a execução dos notebooks de machine learning usando o jupyter notebooks para criar o modelo necessário para realizar inferência na API.

**Requisitos: Conta AWS com uma VPC default ou outra configurada corretamente, AWS CLI instalada e configurada com as credenciais de acesso de forma default ou com profiles.**

1. Os Notebooks pode ser executado em outros locais diferentes do Jupyter Notebooks, assim como o Jupyter Notebooks também pode ser executado em vários locais. E neste passo a passo, ele será executado no VSCode, aqui está a documentação de [download e configuração do VSCode para python](https://code.visualstudio.com/docs/python/python-quick-start).

2. Após baixar e instalar o VSCode, será necessário instalar e configurar o ambiente do Jupyter notebooks, aqui está a documentação de [configurar o VSCode para o Jupyter Notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

3. Clone e abra projeto no VSCode:

    ```bash
   git clone -b grupo-6 --single-branch https://github.com/Compass-pb-aws-2024-MAIO-A/sprints-4-5-pb-aws-maio.git
   cd sprints-4-5-pb-aws-maio
   code .
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure as variáveis de ambiente:

   Crie um arquivo `.env` na raiz do projeto seguindo o modelo do arquivo de exemplo **[.env.example](.env.example)** do repositório.

6. Certifique-se de que sua AWS CLI está logada corretamente e com as permissões necessárias para poder executar os notebooks localizados na pasta [ml-lab/](ml-lab).

7. Executar os notebooks seguindo a ordem dos arquivos do 0 ao 4, onde será explicado o que cada notebook fará:

    - **00-storage-original-dataset**: Irá ler o dataset.csv, criar uma instância no RDS e depois armazenar o dataset sem modificações no RDS para futuras consultas.

    - **01-exploratory-data-analysis**: Irá ler o dataset armazenado no RDS e fazer a análise dos dados para que os processamentos possam ser feitos.

    - **02-data-processing-and-storage**: Irá fazer os devidos processamentos dos dados analisados e depois inserí-los no RDS em outra tabela.

    - **03-training-xgboost-model**: Irá utilizar os dados processados para o treinamento e teste do modelo com o framework Xgboost no SageMaker, onde será criado um Bucket S3 e uma Role IAM com as permissões requisitadas pelo SageMaker, e os dados de treinamento e teste serão armazenados no S3 junto do modelo que será treinado com esses mesmos dados.

    - **04-prediction-and-evaluation**: Irá fazer o download e descompactação do modelo treinado que foi armazenado no S3, e logo após serão feitas as previsões e avaliações do modelo com a lib sklearn.

    **OBS:** O notebook `00-storage-original-dataset` tem um aviso sobre a parte `02 - Create RDS instance if not exists`, nesta parte tem que esperar a instância do RDS ser processada e ficar em execução para que o endpoint possa ser consultado e utilizado, isso pode ser visto no console AWS, são aproximadamente *5min*.

---

### Passos para execução local da API com Python e Docker

Este guia fornece instruções passo a passo para configurar e fazer a execução da API de inferência no ambiente local após a criação do modelo usando os notebooks deste projeto seguindo os passos acima.

1. **Preparação do modelo para inferência**:

    Executar o script **[prepare_model.py](scripts/prepare_model.py)** que irá buscar no bucket S3 definido nas variáveis de ambiente, o último modelo que foi treinado usando os notebooks desse projeto, e irá baixá-lo e descompactá-lo para que seja utilizado na inferência. Para executar o script, use:

    ```bash
    python scripts/prepare_model.py
    ```

2.
   1. **Execução local com Python**:

      ```bash
      python api/main.py
      ```

   2. **Build e execução local com Docker Compose**:

      ```bash
      docker compose up -d
      ```

3. **Acesse a aplicação**:

   Abra o navegador e vá para `http://localhost:8000/docs` nas execuções via Python ou `http://localhost/docs` nas execuções via Docker para acessar a interface do **Swagger** onde haverá um modelo com instruções para utilizar a API.

---

### Passos para o deploy com o EC2 e Docker

Este guia fornece instruções para configurar e fazer o deploy da imagem Docker da API de inferência no AWS EC2 via AWS CLI, e que também pode ser feito via console da AWS.

Para mais informações sobre os comandos e flags fornecidas no passo a passo, além de outros comandos, confira a [comandos AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).

1. Na raiz do projeto, fazer o build da imagem docker da aplicação e postá-la no docker hub.

    ```bash
    docker build -t docker-hub-user/inference-image:latest . --no-cache
    docker push docker-hub-user/inference-image:latest

    # OBS: substitua "docker-hub-user" pelo seu nome de usuário do DockerHub.
    ```

2. Editar o script `ec2.sh` localizado em [scripts/ec2.sh](scripts/ec2.sh) para alterar a imagem de criação do container baseado repositório docker hub, ex: `fulano/inference-image:latest`.

3. Configurar um Security Group com a porta `HTTP 80` liberada para `0.0.0.0/0` na VPC padrão ou em outra.

4. Executar uma instância EC2 com associação de um ip público passando o script `ec2.sh` editado com os valores corretos e definindo a VPC e o Security Group explícitos caso não sejam os default.

   ```bash
   aws ec2 run-instances \
   --image-id ami-08a0d1e16fc3f61ea \
   --count 1 \
   --instance-type t2.micro \
   --associate-public-ip-address \
   --user-data file://scripts/ec2.sh \
   --tag-specifications ResourceType=instance,Tags='[{Key=Project,Value=project},{Key=CostCenter,Value=costcenter},{Key=Name,Value=movies-mania}]' \
   ResourceType=volume,Tags='[{Key=Project,Value=project},{Key=CostCenter,Value=costcenter},{Key=Name,Value=movies-mania}]' \
   --profile profile_name

   # a flag --profile aqui só é necessária caso o perfil usado não seja o default
   # neste caso, substitua "profile-name" pelo nome do seu profile
   ```

5. Aguardar a criação da instância e configuração do container, e depois de alguns minutos acessar o ip público da instância que pode ser visto acessando a instância em execução na página das instâncias EC2 no console AWS.

## 🧱 Estrutura do projeto
```plaintext
.
├── .venv/
├── api/
├── assets/
├── ml-lab/
│   ├── dataset/
│   ├── env/
│   ├── iam/
│   ├── rds/
│   ├── s3/
├── scripts/
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── dockerfile
├── README.md
├── requirements.txt
```
---
- **.venv/** - Contém as dependência do sistema.
- **api/** - Contém as rotas, esquemas e utilitários da API.
- **assets/** - Contém os diagramas dos esquemas de arquitetura e do dataset.
- **ml-lab/** - Contém os notebooks responsáveis pela análise e tratamento de dados além da criação do modelo.
  - **dataset/** - Contém o dataset base.
  - **env/** - Contém variáveis de ambiente relacionadas a configuração dos serviços AWS.
  - **iam/** - Contém scripts para a criação, anexação e recuperação de roles IAM.
  - **rds/** - Contém scripts para a criação da engine do rds bem como a crição e obtenção de instâncias.
  - **s3/** - Contém scripts para a criação de uma instância S3.
- **scripts/** - Contém scipts utilitários para a execução do docker e a preparação do modelo para uso.
- **.env** - Arquivo de configuração das variáveis de ambiente.
- **.env.example** - Exemplo do arquivo `.env` com as variáveis de ambiente necessárias.
- **.gitignore** - Arquivo de configuração para ignorar arquivos no Git.
- **docker-compose.yml** - Arquivo de configuração para construção e execução do projeto com Docker Compose.
- **Dockerfile** - Arquivo de configuração para a construção da imagem Docker.
- **README.md** - Documentação do projeto.
- **requirements.txt** - Arquivo contendo quais dependências são instaladas no projeto bem como suas respectivas versões
## 🚧 Desafios e Soluções

### Compreenção do problema
Levamos um tempo para compreender a proposta da sprint. Revisitando algumas vezes o readmen e tirando algumas dúvidas nas dailys conseguimos compreender melhor

### Concepção da Solução
Foi bastante demorado a concepção da solução pois não soubemos imediatamente como solucionaríamos o problema, como por exemplo que algoritmo de aprendizado usaríamos ou como processaríamos e analisaríamos os dados.

### Integração com os Serviços AWS em Ambiente Local
Era requisito usarmos o sagemaker localmente para evitar custos extras, sendo assim tivemos que fazer um esforço extra para descobrir como integrar os serviços aws ao nosso ambiente local

## Inferência
Enfretamos um problema com a inferência onde de acordo com a ordem dos dados inseridos o resultado mudava drasticamente 

## 👥 Contribuidores

- **[João Guilherme](https://github.com/Joao-Patriota)**
- **[Richard Freitas](https://github.com/wesleyfreit)**
- **[Ytallo Alves](https://github.com/YtalloAlves)**
