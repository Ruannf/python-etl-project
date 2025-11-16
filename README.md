# ETL Pipeline em Python para Carga de Dados no SQL Server

Este projeto implementa um pipeline **ETL completo (Extract → Transform → Load)** utilizando **Python, Pandas e SQLAlchemy**, com o objetivo de automatizar a ingestão de dados provenientes de arquivos CSV para uma tabela SQL Server.

O código foi estruturado seguindo boas práticas de Engenharia de Dados, permitindo fácil manutenção, expansão e integração com orquestradores.

---

## 📑 Índice

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

## 📊 Visão Geral

O pipeline realiza:

- **Leitura** segura de um CSV
- **Tratamento e padronização** dos dados
- **Transformações** (datas, booleanos, renomeações)
- **Inserção** no banco SQL Server com tratamento de erros
- **Registro de logs** detalhados de todas as etapas do processo

---

## 🏗️ Arquitetura do Projeto

