# 🚀 Instalação e Setup

Este guia descreve os passos necessários para configurar o ambiente de desenvolvimento e instalar todas as dependências do projeto.

## Pré-requisitos

Antes de começar, garanta que você tenha as seguintes ferramentas instaladas em seu sistema:

* **Python:** É necessário ter a versão `3.11` ou superior. Você pode baixar a versão mais recente no [site oficial do Python](https://www.python.org/downloads/).
* **Poetry:** Utilizamos o Poetry para gerenciar as dependências do projeto e o ambiente virtual. Se você não o tiver instalado, siga as instruções de instalação no [site oficial do Poetry](https://python-poetry.org/docs/#installation).

## Passo a Passo da Instalação

Com os pré-requisitos atendidos, siga os passos abaixo para instalar o projeto.

1.  **Clonar o Repositório**

    Abra seu terminal ou Git Bash e clone o repositório do projeto para a sua máquina local:

    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Acessar a Pasta do Projeto**

    Navegue até o diretório que acabou de ser criado:

    ```bash
    cd seu-repositorio
    ```

3.  **Instalar as Dependências**

    Com o Poetry instalado, execute o comando a seguir. Ele irá ler o arquivo `pyproject.toml`, resolver as dependências, criar um ambiente virtual isolado para o projeto e instalar tudo o que é necessário (`pandas`, `pydantic`, `mkdocs`, etc.).

    ```bash
    poetry install
    ```

Pronto! Ao final desses passos, o ambiente estará completamente configurado e pronto para a execução do pipeline.