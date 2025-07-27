# 🚗 API de Revenda de Veículos - Autenticação Usuários

Esta aplicação foi criada utilizando Python 3.10 e é utilizada para cadastro e login de clientes da Revenda de Veículos.e. O código foi desenvolvido para ser executado em uma função AWS Lambda, com o API Gateway da AWS atuando como trigger para as requisições. O sistema é focado na administração de usuários e controle de acessos, utilizando o Amazon Cognito para implementar o gerenciamento de grupos e usuários, garantindo uma abordagem escalável e segura para controle de permissões.

---

## 🧰 Tecnologias utilizadas

- **FastAPI** – framework web moderno e rápido
- **Pydantic** – validação de dados
- **AWS Cognito** – autenticação de usuários
- **Docker** - execar as aplicações

---

## 📌 Endpoints principais

### 🔍 Cadastrar usuário

`POST /api/signup`

### 🔍 Confirmar cadastro

`GET /api/confirm`

É necessário confirmar o cadastro para continuar com o login. Para fins de teste, utilize o gerador de emails temporário disponível em https://www.invertexto.com/gerador-email-temporario
### 🔍 Fazer login

`GET /api/login`


## 🚀 Como executar
Para rodar o serviço certifique-se de ter o Python 3.9 instalado em sua máquina. Além disso, instale as dependências do projeto utilizando `pip`:
```bash
pip install -r requirements.txt
```
Além disso, é necessário adicionar as variáveis de ambiente que se encontram no arquivo `.env`. As variáveis de ambiente incluem configurações como região da AWS, ID do pool de usuários, ID do cliente, entre outras.

```env
    awsRegion=us-east-1
    userPoolId=
```

Com o objetivo de facilitar o testes, utilizar os valores abaixo:
```
COGNITO_USER_POOL_ID=us-east-1_dM4m7f4os

COGNITO_APP_CLIENT_ID=296unjdo8l02av4neefc9mo0tl

awsClientCognito=cognito-idp
```

Foi adicionado um usuário também para testes, cujo username é 48250275047 e senha Teste!123

Os cpfs utilizados foram gerados através da plataforma de teste: https://www.geradordecpf.org/

---

## 📑 Documentação da API

- Swagger: [http://localhost:8080/docs](http://localhost:8080/docs)

---

## ‍💻 Repositório
   https://github.com/ketlinfabri/auth-api

## ‍💻 Desenvolvido por

Ketlin Fabri dos Santos  - rm354534 | Trabalho Fase 3