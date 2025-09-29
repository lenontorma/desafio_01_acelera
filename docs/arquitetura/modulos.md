# 🧩 Módulos do Código (src)

O diretório `/src` contém a lógica ETL do projeto, dividida em módulos por responsabilidade.

---

## `src/extract_data.py`

* **Responsabilidade:** Leitura do arquivo CSV de entrada.
* **Função Principal:** `extrair_dados(caminho_do_arquivo: str) -> pd.DataFrame`
* **Ações:**
    1.  Lê o arquivo CSV a partir do caminho fornecido.
    2.  Retorna os dados como um DataFrame Pandas.
    3.  Interrompe a execução se o arquivo não for encontrado ou estiver vazio.

---

## `src/transform_data.py`

* **Responsabilidade:** Validação de dados e separação de registros.
* **Componente Principal:** `FuncionarioModel` (Pydantic)
    * Define a estrutura e as regras de validação para um registro de funcionário.
* **Função Principal:** `transformar_dados(df_bruto: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]`
* **Ações:**
    1.  Itera sobre cada linha do DataFrame de entrada.
    2.  Valida cada linha contra o modelo `FuncionarioModel`.
    3.  Para registros válidos, calcula o bônus e os armazena.
    4.  Para registros inválidos, armazena o registro original e a mensagem de erro.
    5.  Retorna dois DataFrames: `dados_validos` e `dados_invalidos`.

---

## `src/load_data.py`

* **Responsabilidade:** Geração dos arquivos de saída (relatórios e KPIs).
* **Função Principal:** `carregar_dados(df_bruto: pd.DataFrame, df_validos: pd.DataFrame, df_invalidos: pd.DataFrame, pasta_output: str)`
* **Ações:**
    1.  Cria o diretório `/output` se não existir.
    2.  Salva o DataFrame de dados válidos em `relatorio_individual.csv`.
    3.  Salva o DataFrame de dados inválidos em `erros.csv`.
    4.  Calcula os KPIs definidos a partir dos DataFrames recebidos.
    5.  Salva os KPIs em formato JSON no arquivo `kpis.json`.