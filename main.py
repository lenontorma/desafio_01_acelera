import os
from src.extract_data import extrair_dados
from src.transform_data import transformar_dados
from src.load_data import carregar_dados

# --- Constantes ---
ARQUIVO_ENTRADA = "data/funcionarios.csv"
PASTA_OUTPUT = "output"

def main():
    """
    Função principal que orquestra o pipeline de ETL completo.
    """
    print("--- Iniciando pipeline de processamento de dados ---")

    # Etapa 1: Extração
    dados_brutos = extrair_dados(caminho_do_arquivo=ARQUIVO_ENTRADA)

    if dados_brutos is None or dados_brutos.empty:
        print("\nPipeline encerrado devido a erro ou arquivo vazio na extração.")
        return

    print("✅ Extração concluída.")
    
    # Etapa 2: Transformação
    dados_validos, dados_invalidos = transformar_dados(dados_brutos)

    print("✅ Transformação concluída.")

    # Etapa 3: Carregamento
    carregar_dados(
        df_bruto=dados_brutos,
        df_validos=dados_validos,
        df_invalidos=dados_invalidos,
        pasta_output=PASTA_OUTPUT
    )

    print("\n--- Pipeline de processamento de dados finalizado com sucesso! ---")
    print(f"Verifique os arquivos gerados no diretório: '{os.path.abspath(PASTA_OUTPUT)}'")


if __name__ == "__main__":
    main()