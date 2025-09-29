# 🚀 Instalação e Setup

Este guia descreve as ferramentas e os passos necessários para interagir com o projeto.

## Ferramentas Necessárias

Dependendo do seu objetivo, você precisará de ferramentas diferentes.

### Para Execução Padrão

Se o seu objetivo é apenas **executar o pipeline** de forma padronizada, você só precisa de uma ferramenta:

* **Docker:** Garante que o pipeline rode em um ambiente isolado e consistente. Você pode baixar a versão mais recente no [site oficial do Docker](https://www.docker.com/products/docker-desktop/).

### Para Desenvolvimento Local

Se você pretende **modificar o código-fonte**, contribuir com o projeto ou rodar os componentes localmente sem o Docker, você precisará de:

* **Python:** Versão `3.11` ou superior. [Download aqui](https://www.python.org/downloads/).
* **Poetry:** Para gerenciamento de dependências. [Instruções de instalação aqui](https://python-poetry.org/docs/#installation).

---

## Passos para Setup de Desenvolvimento

Estes passos são para quem deseja configurar um ambiente de desenvolvimento local (opção "Para Desenvolvimento Local" acima).

1.  **Clonar o Repositório**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Acessar a Pasta do Projeto**
    ```bash
    cd seu-repositorio
    ```

3.  **Instalar as Dependências com Poetry**
    Este comando cria um ambiente virtual e instala todas as bibliotecas necessárias para o desenvolvimento.
    ```bash
    poetry install
    ```

Com isso, seu ambiente de desenvolvimento local estará pronto. Para as instruções de como rodar o projeto, consulte a página [Como Executar](./execucao.md).