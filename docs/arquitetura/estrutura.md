# 🧩 Estrutura de Pastas e Arquivos

Esta seção detalha a organização do projeto, explicando o propósito de cada diretório e arquivo principal. Uma estrutura bem definida é fundamental para a manutenibilidade e escalabilidade do código.

## Mapa do Projeto

A estrutura de alto nível do projeto é a seguinte, refletindo a separação de responsabilidades entre dados, código-fonte, documentação e saídas.

desafio_01                      
├─ data                         
│  └─ funcionarios.csv          
├─ docs                         
│  ├─ arquitetura               
│  │  ├─ estrutura.md           
│  │  └─ modulos.md             
│  ├─ guia                      
│  │  ├─ execucao.md            
│  │  └─ instalacao.md          
│  ├─ regras                    
│  │  ├─ bonus.md               
│  │  └─ validacao.md           
│  ├─ index.md                  
│  └─ outputs.md                
├─ output                       
│  ├─ erros.csv                 
│  ├─ kpis.json                 
│  └─ relatorio_individual.csv  
├─ src                          
│  ├─ extract_data.py           
│  ├─ load_data.py              
│  └─ transform_data.py         
├─ desafio_01.md                
├─ Dockerfile                   
├─ main.py                      
├─ mkdocs.yml                   
├─ poetry.lock                  
└─ pyproject.toml               



## Descrição dos Componentes

### Pastas

* **`/data`**: Contém os dados brutos de entrada para o pipeline.
* **`/docs`**: Contém os arquivos-fonte (em formato Markdown) para a documentação do projeto.
* **`/output`**: Diretório onde todos os artefatos gerados pelo pipeline são salvos.
* **`/src`**: Contém o código-fonte do pipeline, dividido em módulos por responsabilidade (ETL).

### Arquivos Principais

* **`main.py`**: Ponto de entrada ("entrypoint") da aplicação. Orquestra a execução do pipeline.
* **`Dockerfile`**: Define os passos para construir a imagem Docker do projeto, garantindo um ambiente de execução portável e consistente.
* **`desafio_01.md`**: Arquivo com o enunciado e os requisitos originais do desafio.
* **`mkdocs.yml`**: Arquivo de configuração do site de documentação gerado pelo MkDocs.
* **`pyproject.toml`**: Arquivo de configuração do Poetry, que declara as dependências do projeto.
* **`poetry.lock`**: Arquivo que garante a instalação das versões exatas de cada dependência, assegurando a reprodutibilidade do ambiente de desenvolvimento.
