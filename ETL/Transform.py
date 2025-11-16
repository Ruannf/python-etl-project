import pandas as pd
from datetime import datetime
import os
import getpass

def transformar_para_insert(df: pd.DataFrame) -> pd.DataFrame:
    print("🧹 Aplicando transformações e padronizações no DataFrame...")

    try:
    # Adiciona colunas de controle de upload
        df['UPLOAD_DATE'] = datetime.today().date()
        df['UPLOAD_BY'] = os.getenv('USUARIO_UPLOAD', getpass.getuser())
    except Exception as e:
        print(f"Erro ao aplicar transformações: \n{e}")
        return df

    print(f"📦 {len(df)} registros prontos para inserção.")
    return df
