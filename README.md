# ETL Pipeline em Python para Carga de Dados no SQL Server

Este projeto implementa um pipeline **ETL completo (Extract → Transform → Load)** utilizando **Python, Pandas e SQLAlchemy**, com o objetivo de automatizar a ingestão de dados provenientes de arquivos CSV para uma tabela SQL Server.

O código foi estruturado seguindo boas práticas de Engenharia de Dados, permitindo fácil manutenção, expansão e integração com orquestradores.

---

## 📑 Índice

## Índice
- [Visão Geral](#visão-geral)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Como Executar](#como-executar)
- [Configuração do Ambiente (.env)](#configuração-do-ambiente-env)
- [Exemplo de Dados](#exemplo-de-dados)
- [Logs do Pipeline](#logs-do-pipeline)
- [Melhorias Futuras](#melhorias-futuras)


---

## Visão Geral

O pipeline realiza:

- **Leitura** segura de um CSV
- **Tratamento e padronização** dos dados
- **Transformações** (datas, booleanos, renomeações)
- **Inserção** no banco SQL Server com tratamento de erros
- **Registro de logs** detalhados de todas as etapas do processo

---

## Arquitetura do Projeto
CSV → Extract (Pandas) → Transform → Load (SQLAlchemy) → SQL Server

---

## Tecnologias Utilizadas

- **Python 3.11+**
- **Pandas**
- **SQLAlchemy**
- **PyODBC**
- **python-dotenv**
- **SQL Server**
- **VSCode** (desenvolvimento)

---

## Funcionalidades

### ✔ Extract
- Leitura do CSV com validações
- Tratamento de arquivos vazios ou inexistentes
- Padronização automática dos nomes das colunas
- Conversão inicial de tipos

### ✔ Transform
- Renomeação de colunas para padrão do banco
- Ajuste de datas
- Conversão de campos booleanos
- Inclusão de metadados:
  - `UPLOAD_DATE`
  - `UPLOAD_BY`

### ✔ Load
- Conexão com SQL Server via SQLAlchemy + PyODBC
- Inserção com `if_exists='append'`
- Logs claros sobre sucesso e falha
- Tratamento de exceções

---

## Estrutura de Pastas

ETL/
├── Main.py # Orquestra o pipeline completo
├── Extract.py # Funções de extração
├── Transform.py # Funções de transformação
├── Load.py # Funções de carga
├── arquivos/
│ └── employees_data.csv
├── acesso.env # Variáveis de ambiente
└── README.md

---

## ▶ Como Executar

### 1️⃣ Criar ambiente virtual (opcional, recomendado)

python -m venv venv
venv\Scripts\activate   # Windows

### 2️⃣ Dependências do Projeto
Python 3.x
Pandas — leitura e manipulação de dados
SQLAlchemy — engine e conexão com SQL Server
PyODBC — driver ODBC para integração com SQL Server
Python-dotenv — carregamento de variáveis de ambiente

### 3️⃣ Configurar variáveis de ambiente
Crie um arquivo acesso.env:

DRIVER=ODBC Driver 17 for SQL Server
SERVER=SEU_SERVIDOR
DATABASE=SUA_BASE
UID=SEU_USUARIO
PWD=SUA_SENHA
USUARIO_UPLOAD=SEU_NOME

### 4️⃣ Executar o pipeline
python Main.py

### Logs do Pipeline

🟦 Iniciando processo ETL...
📥 Extraindo dados do CSV tratado...
✔ 100 linhas extraídas com sucesso.
🛠 Aplicando transformações e padronizações no DataFrame...
✔ 100 registros prontos para inserção.
📤 Iniciando etapa de upload para o banco...
✔ 100 registros inseridos na tabela [TBL_EMPLOYEES].
🏁 Processo ETL finalizado com sucesso!

