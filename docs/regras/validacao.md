# 📖 Regras de Validação dos Dados

Este documento centraliza todas as regras de negócio utilizadas para validar cada registro do arquivo `funcionarios.csv`. **A automação da validação destas regras são realizadas através de um contrato de dados definido com a biblioteca Pydantic.**

## Campo: `nome`

* **Regra 1:** O valor não pode ser vazio ou conter apenas espaços em branco.
* **Regra 2:** O valor não pode conter caracteres numéricos (`0-9`).

---

## Campo: `area`

* **Regra 1:** O valor deve corresponder exatamente a uma das seguintes opções:
    * `Vendas`
    * `TI`
    * `Financeiro`
    * `RH`
    * `Operações`

---

## Campo: `salario`

* **Regra 1:** O valor deve ser um número.
* **Regra 2:** O valor deve ser maior ou igual a zero (`>= 0`).

---

## Campo: `bonus_percentual`

* **Regra 1:** O valor deve ser um número.
* **Regra 2:** O valor deve estar no intervalo entre 0 e 1, inclusive (`0 <= valor <= 1`).