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

## 2. Execução via Docker (Recomendado para Execução Padrão)

Esta é a forma recomendada de executar o pipeline para garantir que ele rode em um ambiente limpo e consistente, sem depender das configurações da sua máquina local.

### Passo 1: Construir a Imagem Docker

Primeiro, você precisa "empacotar" a aplicação em uma imagem Docker. Este comando precisa ser executado apenas uma vez ou sempre que o código-fonte for alterado.

```bash
docker build -t pipeline-funcionarios .
  ```
### Passo 2: Executar o Pipeline via Container
Com a imagem construída, você pode executar o pipeline a qualquer momento com o seguinte comando. Ele utiliza volumes para compartilhar as pastas data (entrada) e output (saída) entre sua máquina e o container.

```bash
docker run --rm \
  -v "$(pwd)/data:/app/data" \
  -v "$(pwd)/output:/app/output" \
  pipeline-funcionarios
```
Este comando executa o pipeline de forma isolada e, ao final, os relatórios estarão disponíveis na sua pasta output/ local, como na execução tradicional.

