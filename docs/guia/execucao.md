# ▶️ Como Executar

Este projeto foi projetado para ser executado de duas maneiras distintas, dependendo da sua necessidade: localmente para desenvolvimento ou via Docker para uma execução padronizada e portável. Certifique-se de ter preparado o ambiente correto conforme o guia de [Instalação e Setup](./instalacao.md).

---

## 1. Execução Local

Esta abordagem é recomendada enquanto você estiver desenvolvendo, testando novas funcionalidades ou depurando o código.

### Executando o Pipeline de Dados

Para executar o pipeline completo de extração, transformação e carga, utilize o Poetry.

1.  **Ative o Ambiente Virtual (Opcional, mas recomendado):**
    Para facilitar, você pode ativar o shell do ambiente virtual do Poetry.
    ```bash
    poetry shell
    ```

2.  **Execute o Script Principal:**
    Uma vez dentro do shell (ou usando `poetry run`), execute o arquivo `main.py`.
    ```bash
    python main.py
    ```

Ao final da execução, a pasta `output/` será criada (ou atualizada) na raiz do projeto com todos os relatórios gerados.

### Visualizando a Documentação

Para visualizar este site de documentação em seu navegador:

1.  **Inicie o Servidor do MkDocs:**
    ```bash
    mkdocs serve
    ```

2.  **Acesse o Site:**
    Abra seu navegador e acesse o endereço [http://localhost:8000](http://localhost:8000). O site será recarregado automaticamente sempre que você salvar uma alteração nos arquivos de documentação.

---

## 2. Execução Universal com Docker Compose (Recomendado)

Esta é a forma recomendada de executar o pipeline. O Docker Compose fornece um comando único e universal que funciona da mesma forma em Windows, macOS e Linux.

### Pré-requisitos

* [Docker e Docker Compose](https://www.docker.com/products/docker-desktop/) instalados e em execução.

### Executando o Pipeline

Com o arquivo de entrada `funcionarios.csv` na pasta `/data`, execute o seguinte comando na raiz do projeto:

```bash
docker-compose run --rm pipeline