import pandas as pd
import sys

def extrair_dados(caminho_do_arquivo: str) -> pd.DataFrame:
    """
    Extrai dados de um arquivo CSV e os carrega em um DataFrame do pandas.

    Args:
        caminho_do_arquivo (str): O caminho completo para o arquivo CSV.

    Returns:
        pd.DataFrame: Um DataFrame do pandas contendo os dados do arquivo.
                      Retorna um DataFrame vazio se o arquivo estiver vazio.
                      O programa é encerrado se o arquivo não for encontrado 
                      ou ocorrer outro erro de leitura.
    """
    try:
        print(f"Iniciando a leitura do arquivo: {caminho_do_arquivo}")
        df = pd.read_csv(caminho_do_arquivo)
        print("Arquivo lido com sucesso.")
        return df
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.", file=sys.stderr)
        sys.exit(1) # Encerra o programa com um código de erro
        
    except pd.errors.EmptyDataError:
        print(f"Aviso: O arquivo '{caminho_do_arquivo}' está vazio.", file=sys.stderr)
        return pd.DataFrame() # Retorna um DataFrame vazio
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}", file=sys.stderr)
        sys.exit(1)