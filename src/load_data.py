import pandas as pd
import json
import os
# Importamos o Enum para ter acesso às áreas válidas
from src.transform_data import AreaEnum 

def carregar_dados(df_bruto: pd.DataFrame, df_validos: pd.DataFrame, df_invalidos: pd.DataFrame, pasta_output: str):
    """
    Salva os DataFrames, calcula KPIs com base na validade de campo e salva os relatórios.

    Args:
        df_bruto (pd.DataFrame): DataFrame original com todos os dados.
        df_validos (pd.DataFrame): DataFrame com os dados 100% válidos.
        df_invalidos (pd.DataFrame): DataFrame com os dados inválidos.
        pasta_output (str): O caminho para a pasta onde os relatórios serão salvos.
    """
    print("\n--- Iniciando fase de carregamento e geração de relatórios ---")
    
    try:
        os.makedirs(pasta_output, exist_ok=True)
        print(f"Diretório '{pasta_output}' pronto para receber os arquivos.")
    except OSError as e:
        print(f"Erro ao criar o diretório '{pasta_output}': {e}")
        return

    caminho_relatorio_individual = os.path.join(pasta_output, "relatorio_individual.csv")
    caminho_erros = os.path.join(pasta_output, "erros.csv")
    caminho_kpis = os.path.join(pasta_output, "kpis.json")

    # --- Geração de arquivos CSV (lógica inalterada) ---
    if not df_validos.empty:
        df_validos.to_csv(caminho_relatorio_individual, index=False, sep=';', encoding='utf-8-sig')
        print(f"✅ Relatório individual gerado em: '{caminho_relatorio_individual}'")

    if not df_invalidos.empty:
        df_invalidos.to_csv(caminho_erros, index=False, sep=';', encoding='utf-8-sig')
        print(f"✅ Relatório de erros gerado em: '{caminho_erros}'")
    
    # --- Cálculo de KPIs (Lógica Refatorada) ---
    print("Calculando KPIs com validação a nível de campo...")

    # KPI 1: Quantidade de funcionários por área
    areas_validas = [item.value for item in AreaEnum]
    df_areas_validas = df_bruto[df_bruto['area'].isin(areas_validas)]
    qtd_por_area = df_areas_validas['area'].value_counts().to_dict()

    # KPI 2: Média de salário por área
    df_bruto['salario_numerico'] = pd.to_numeric(df_bruto['salario'], errors='coerce')
    df_salarios_validos = df_bruto[
        df_bruto['area'].isin(areas_validas) &
        df_bruto['salario_numerico'].notna() &
        (df_bruto['salario_numerico'] >= 0)
    ]
    media_salario_area = df_salarios_validos.groupby('area')['salario_numerico'].mean().round(2).to_dict()
    
    # KPIs 3 e 4: Bônus total e Top 3 bônus
    bonus_total = 0
    top_3_bonus = []
    if not df_validos.empty:
        bonus_total = round(df_validos['bonus_final'].sum(), 2)
        top_3_bonus = df_validos.nlargest(3, 'bonus_final')[['nome', 'bonus_final']].to_dict('records')
    else:
        print("⚠️ KPIs de bônus não gerados pois não há dados 100% válidos.")

    kpis = {
        "quantidade_funcionarios_por_area": qtd_por_area,
        "media_salario_por_area": media_salario_area,
        "bonus_total_geral": bonus_total,
        "top_3_funcionarios_maior_bonus": top_3_bonus
    }

    with open(caminho_kpis, 'w', encoding='utf-8') as f:
        json.dump(kpis, f, indent=4, ensure_ascii=False)
    print(f"✅ Relatório de KPIs (com lógica aprimorada) gerado em: '{caminho_kpis}'")