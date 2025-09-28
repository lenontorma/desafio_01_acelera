import pandas as pd
from pydantic import BaseModel, Field, field_validator, ValidationError
from enum import Enum

# Definição dos Modelos e Regras de Negócio (O Contrato Pydantic)

class AreaEnum(str, Enum):
    """Enum para garantir que a área seja uma das opções válidas."""
    VENDAS = "Vendas"
    TI = "TI"
    FINANCEIRO = "Financeiro"
    RH = "RH"
    OPERACOES = "Operações"

class FuncionarioModel(BaseModel):
    """Modelo Pydantic que define a estrutura e as regras de um funcionário válido."""
    nome: str
    area: AreaEnum
    salario: float = Field(ge=0, description="Salário não pode ser negativo.")
    bonus_percentual: float = Field(ge=0, le=1, description="Bônus deve ser entre 0 e 1.")

    @field_validator('nome')
    def validar_nome(cls, v: str) -> str:
        """Valida se o nome não está vazio e não contém números."""
        if not v.strip():
            raise ValueError('O nome não pode ser vazio.')
        if any(char.isdigit() for char in v):
            raise ValueError('O nome não pode conter números.')
        return v.strip()

BONUS_BASE = 1000

def transformar_dados(df_bruto: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Valida, transforma e separa os dados de funcionários.

    Args:
        df_bruto (pd.DataFrame): DataFrame com os dados brutos extraídos.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: Uma tupla contendo dois DataFrames:
                                           1. DataFrame com registros válidos e bônus calculado.
                                           2. DataFrame com registros inválidos e o motivo do erro.
    """
    registros_validos = []
    registros_invalidos = []

    print("\n--- Iniciando fase de transformação e validação ---")
    for index, linha in df_bruto.iterrows():
        try:
            # 1. Tenta validar a linha usando o modelo Pydantic
            dados_linha = linha.to_dict()
            funcionario_validado = FuncionarioModel(**dados_linha)

            # 2. Se a validação passar, calcula o bônus
            bonus = BONUS_BASE + (funcionario_validado.salario * funcionario_validado.bonus_percentual)
            
            # 3. Adiciona o bônus ao registro e o insere na lista de válidos
            registro_processado = funcionario_validado.model_dump()
            registro_processado['bonus_final'] = round(bonus, 2)
            registros_validos.append(registro_processado)

        except ValidationError as e:
            # 4. Se a validação falhar, captura o erro
            registro_original = linha.to_dict()
            erros = e.errors()
            # Formata a mensagem de erro para ser mais legível
            motivo_erro = f"Campo '{erros[0]['loc'][0]}': {erros[0]['msg']}"
            
            registro_original['motivo_do_erro'] = motivo_erro
            registros_invalidos.append(registro_original)

    print(f"Validação concluída: {len(registros_validos)} registros válidos, {len(registros_invalidos)} registros inválidos.")
    
    # Converte as listas de dicionários de volta para DataFrames
    df_validos = pd.DataFrame(registros_validos)
    df_invalidos = pd.DataFrame(registros_invalidos)

    return df_validos, df_invalidos