import pandas as pd

def extract_from_csv(caminho_arquivo: str) -> pd.DataFrame:
    """
    Extrai e trata dados de um arquivo CSV.
    - Renomeia colunas
    - Converte tipos
    - Retorna DataFrame pronto para carga no banco
    """
    print("📥 Extraindo dados do CSV tratado...")

    # 1. Leitura do CSV
    try:
        df = pd.read_csv(caminho_arquivo)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print("O arquivo CSV está vazio.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro ao ler o CSV:\n{e}")
        return pd.DataFrame()

    # 2. Processamento
    try:
        # Padroniza nomes das colunas
        df.columns = (
            df.columns.str
            .strip()          # remove espaços
            .str.upper()       # caixa alta
            .str.replace(" ", "_")  # substitui espaço por _
        )
        
        # Renomeia colunas para padrão do banco
        df.rename(columns={
            'NAME': 'NOME',
            'DATE': 'DATA_RE',
            'COMPANY': 'EMPRESA',
            'BOOLEAN': 'ATIVO'
        }, inplace=True)

        # Conversões
        df['DATA_RE'] = pd.to_datetime(df['DATA_RE'], errors='coerce')
        df['ATIVO'] = df['ATIVO'].map({'Yes': True, 'No': False})

    except Exception as e:
        print(f"❌ Erro ao transformar os dados no extract:\n{e}")
        return pd.DataFrame()

    # Resultado final
    print(f"✅ {len(df)} linhas extraídas com sucesso.")

    return df
