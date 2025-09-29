# Pipeline de Dados: Processamento de Funcionários


Este projeto implementa um pipeline de ETL (Extração, Transformação e Carga) para processar um arquivo CSV com dados de funcionários. O pipeline realiza a validação de cada registro, calcula bônus e gera relatórios de saída, incluindo um arquivo de erros e um resumo de KPIs.

O projeto é totalmente containerizado com Docker para garantir a portabilidade e a reprodutibilidade da execução.

---

## ✨ Funcionalidades Principais

* **Extração de Dados:** Lê dados de arquivos `.csv`.
* **Validação:** Utiliza Pydantic para criar um "contrato de dados", garantindo a integridade e a qualidade dos registros.
* **Processamento Lógico:** Calcula bônus com base em regras de negócio predefinidas.
* **Geração de Relatórios:** Cria arquivos de saída separados para dados válidos (`.csv`), erros (`.csv`) e KPIs (`.json`).
* **Containerização:** Empacotado com Docker para uma execução consistente em qualquer ambiente.
* **Documentação Completa:** Acompanhado por um site de documentação gerado com MkDocs.

---

## 🛠️ Tecnologias Utilizadas


<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic"/>
  <img src="https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white" alt="Poetry"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/MkDocs-4A4A4A?style=for-the-badge&logo=markdown&logoColor=white" alt="MkDocs"/>
</p>

---
---

## 🚀 Executando o Pipeline (Modo Padrão com Docker)

Esta é a forma recomendada para executar o projeto.

### Pré-requisitos

* [Docker](https://www.docker.com/products/docker-desktop/) instalado e em execução.

### Passos

1.  **Clone este repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2.  **Prepare o arquivo de entrada:**
    Coloque o arquivo `funcionarios.csv` que você deseja processar dentro da pasta `/data`.

3.  **Construa a imagem Docker:**
    Este comando lê o `Dockerfile` e empacota a aplicação.
    ```bash
    docker build -t pipeline-funcionarios .
    ```

4.  **Execute o pipeline:**
    Este comando executa o container. Ele mapeia as pastas locais `data` e `output` para dentro do container, permitindo que o script leia seu arquivo de entrada e escreva os resultados de volta na sua máquina.
    ```bash
    docker run --rm \
      -v "$(pwd)/data:/app/data" \
      -v "$(pwd)/output:/app/output" \
      pipeline-funcionarios
    ```

Após a execução, os relatórios estarão disponíveis na pasta `/output`.

---

## 📖 Documentação

Para uma visão detalhada da arquitetura, regras de negócio, e guias para desenvolvimento local, consulte a **documentação completa do projeto**.

Para visualizar o site de documentação localmente:

1.  **Instale as dependências de desenvolvimento:**
    ```bash
    poetry install
    ```

2.  **Inicie o servidor do MkDocs:**
    ```bash
    mkdocs serve
    ```

3.  Abra seu navegador e acesse `http://localhost:8000`.

---

## 🧑‍💻 Para Desenvolvedores (Execução Local)

Se você deseja modificar o código ou executá-lo sem Docker, siga as instruções detalhadas na seção **`Guia Rápido > Instalação e Setup`** da documentação.