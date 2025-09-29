# 🏠 Visão Geral do Pipeline de Dados de Funcionários

Este documento serve como um guia central para entender a arquitetura, as regras de negócio e o funcionamento deste projeto, **que é empacotado com Docker para garantir portabilidade e uma execução consistente em qualquer ambiente.**

## O Desafio

O objetivo deste projeto é processar um arquivo `funcionarios.csv` contendo informações de colaboradores de uma empresa. A missão consiste em desenvolver um pipeline de dados robusto que realize a extração, validação, transformação e cálculo de bônus, gerando relatórios claros e métricas de desempenho (KPIs).

## O Fluxo do Pipeline (ETL)

O projeto foi estruturado seguindo o padrão clássico de ETL (Extract, Transform, Load), garantindo modularidade e clareza no processamento dos dados.

1.  **Extract (Extração):** A primeira etapa consiste em ler os dados brutos do arquivo `funcionarios.csv` e carregá-los em memória utilizando a biblioteca Pandas, preparando-os para a fase de transformação.

2.  **Transform (Transformação):** Este é o coração do pipeline. Cada registro de funcionário é submetido a um rigoroso processo de validação de dados utilizando Pydantic para garantir a integridade e a conformidade com as regras de negócio. Os registros são então separados em duas categorias: válidos e inválidos. Para os registros válidos, é calculado o bônus final.

3.  **Load (Carga):** Na última etapa, os dados processados são persistidos em disco. São gerados três artefatos principais: um relatório em CSV com os funcionários válidos e seu bônus, um relatório em CSV com os registros inválidos e o motivo do erro, e um arquivo JSON contendo KPIs agregados.

## Tecnologias Utilizadas

Este projeto foi construído utilizando tecnologias modernas e boas práticas do ecossistema Python para engenharia de dados.

* **Python 3.11+**
* **Pandas:** Para manipulação e análise de dados em alto desempenho.
* **Pydantic:** Para validação de dados robusta e explícita.
* **Poetry:** Para gerenciamento de dependências e do ambiente virtual.
* **Docker:** Para containerização da aplicação, garantindo reprodutibilidade.
* **MkDocs:** Para a geração desta documentação.