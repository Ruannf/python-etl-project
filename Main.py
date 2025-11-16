from sqlalchemy import create_engine
from ETL.Extract import extract_from_csv
from ETL.Transform import transformar_para_insert
from ETL.Load import load_to_sql
from dotenv import load_dotenv
import os

# === Carregar variáveis de ambiente ===
load_dotenv(dotenv_path=r"C:\ETL\acesso.env")

# === Configurações ===
ARQUIVO_CSV = r"C:\ETL\Arquivos\exployees_data.csv"
TABELA_DESTINO = 'TBL_EMPLOYEES'

# === Conexão com o banco ===

CONNECTSTRING = (
    f'DRIVER={os.getenv("DRIVER")};'
    f'SERVER={os.getenv("SERVER")};'
    f'DATABASE={os.getenv("DATABASE")};'
    f'UID={os.getenv("UID")};'
    f'PWD={os.getenv("PWD")};'
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={CONNECTSTRING}")

# === Execução ETL ===
print("Iniciando processo ETL...")

df_extraido = extract_from_csv(ARQUIVO_CSV)
df_pronto = transformar_para_insert(df_extraido)
load_to_sql(df_pronto, engine, TABELA_DESTINO)

print("Processo ETL finalizado com sucesso!")
