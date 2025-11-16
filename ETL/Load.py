def load_to_sql(df, engine, tabela):
    print("🚚 Iniciando etapa de upload para o banco...")

    # Verifica se há dados
    if df.empty:
        print("⚠️ Nenhum dado disponível para upload.")
        return

    # Insere os dados atualizados
    try:
        df.to_sql(tabela, con=engine, if_exists='append', index=False)
        print(f"✅ {len(df)} registros inseridos com sucesso na tabela [{tabela}].")
    except Exception as e:
        print(f"❌ Erro ao inserir os dados no banco:\n{e}")
