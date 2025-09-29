# 📊 Arquivos de Saída

Após a execução bem-sucedida do pipeline, três arquivos são gerados e salvos no diretório `/output`. Esta seção detalha o conteúdo e a estrutura de cada um desses arquivos.

---

## 1. `relatorio_individual.csv`

* **Descrição:** Contém todos os registros de funcionários que passaram com sucesso em todas as etapas de validação.

* **Colunas:**
    * `nome` (str): Nome do funcionário.
    * `area` (str): Área de atuação do funcionário.
    * `salario` (float): Salário base.
    * `bonus_percentual` (float): Percentual de bônus aplicado.
    * `bonus_final` (float): Valor final do bônus calculado (`BONUS_BASE + salario * bonus_percentual`).

---

## 2. `erros.csv`

* **Descrição:** Contém todos os registros que falharam em pelo menos uma regra de validação definida no contrato de dados.

* **Colunas:**
    * Contém todas as colunas originais do arquivo de entrada (`nome`, `area`, `salario`, `bonus_percentual`).
    * `motivo_do_erro` (str): Descreve qual regra de validação falhou e o motivo, conforme retornado pelo Pydantic.

---

## 3. `kpis.json`

* **Descrição:** Arquivo em formato JSON contendo métricas de desempenho (KPIs) agregadas, calculadas a partir dos dados processados.

* **Estrutura do JSON e Descrição das Chaves:**

    ```json
    {
        "quantidade_funcionarios_por_area": {},
        "media_salario_por_area": {},
        "bonus_total_geral": 0.0,
        "top_3_funcionarios_maior_bonus": []
    }
    ```

    * **`quantidade_funcionarios_por_area`**: Dicionário contendo a contagem de funcionários por cada área válida. O cálculo considera todos os registros que possuem um valor de `area` válido.

    * **`media_salario_por_area`**: Dicionário contendo a média salarial para cada área válida. O cálculo considera todos os registros que possuem `area` e `salario` válidos.

    * **`bonus_total_geral`**: Número (float) que representa a soma de todos os valores da coluna `bonus_final` dos funcionários válidos.

    * **`top_3_funcionarios_maior_bonus`**: Lista de dicionários, cada um representando um dos três funcionários com os maiores valores de `bonus_final`, contendo o nome e o valor do bônus.