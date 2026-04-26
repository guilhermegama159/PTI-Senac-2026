# Importação dos dicionários necessários
import pandas as pd
import sqlite3
import os

# Configuração do caminho do banco de dados Titanic
diretorio_atual = os.getcwd()
caminho_db = os.path.join(diretorio_atual, "dados", "titanic.db")

# Conexão com o banco de dados
conn = sqlite3.connect(caminho_db)

try:
    # Localização da tabela
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    resultado = cursor.fetchone()

    if resultado is None:
        print("Erro: O banco de dados não possui tabelas!")

    else:
        nome_tabela = resultado[0]

        # Total de passageiros
        total = pd.read_sql(
            f"SELECT COUNT(*) AS total FROM {nome_tabela}",
            conn
        ).iloc[0, 0]

        # Total de sobreviventes
        sobreviventes = pd.read_sql(
            f"SELECT COUNT(*) AS total FROM {nome_tabela} WHERE Sobreviveu = 1",
            conn
        ).iloc[0, 0]

        # Taxa geral de sobrevivência
        taxa_geral = round((sobreviventes / total) * 100, 2)

        # Quantidade de tickets vendidos
        tickets_unicos = pd.read_sql(
            f"SELECT COUNT(DISTINCT Ticket) AS total FROM {nome_tabela}",
            conn
        ).iloc[0, 0]

        # Total de tarifa arrecadado
        total_tarifa = pd.read_sql(
            f"SELECT SUM(Tarifa) AS total FROM {nome_tabela}",
            conn
        ).iloc[0, 0]

        # Local de embarque mais frequente
        embarque_top = pd.read_sql(f"""
            SELECT Local_Embarque, COUNT(*) AS qtd
            FROM {nome_tabela}
            WHERE Local_Embarque IS NOT NULL AND Local_Embarque != ''
            GROUP BY Local_Embarque
            ORDER BY qtd DESC
            LIMIT 1
        """, conn)

        # Taxa de sobrevivência por sexo
        sexo_stats = pd.read_sql(f"""
            SELECT Sexo,
                   COUNT(*) AS Passageiros,
                   ROUND(AVG(Sobreviveu) * 100, 2) AS "Taxa de Sobrevivencia"
            FROM {nome_tabela}
            GROUP BY Sexo
        """, conn)

        # Taxa de sobrevivência por classe
        classe_stats = pd.read_sql(f"""
            SELECT Classe,
                   COUNT(*) AS Passageiros,
                   ROUND(AVG(Sobreviveu) * 100, 2) AS "Taxa de Sobrevivencia"
            FROM {nome_tabela}
            GROUP BY Classe
            ORDER BY Classe
        """, conn)

        # Distribuição de idade com taxa de sobrevivência
        idade_dist = pd.read_sql(f"""
            SELECT
                CASE
                    WHEN Idade < 18 THEN '0-17 (Criança/Jovem)'
                    WHEN Idade BETWEEN 18 AND 59 THEN '18-59 (Adulto)'
                    WHEN Idade >= 60 THEN '60+ (Idoso)'
                    ELSE 'Não Informada'
                END AS Faixa_Etaria,
                COUNT(*) AS Total,
                ROUND(AVG(Sobreviveu) * 100, 2) AS "Taxa de Sobrevivencia"
            FROM {nome_tabela}
            GROUP BY Faixa_Etaria
            ORDER BY Faixa_Etaria
        """, conn)

        # Comparação sobreviventes vs não sobreviventes
        status_stats = pd.read_sql(f"""
            SELECT
                CASE WHEN Sobreviveu = 1 THEN 'Sobreviveu' ELSE 'Não Sobreviveu' END AS Status,
                COUNT(*) AS Qtd,
                ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM {nome_tabela}), 2) AS Porcentagem
            FROM {nome_tabela}
            GROUP BY Sobreviveu
        """, conn)

        # Resultados principais
        print("=" * 40)
        print("      DADOS ANALISADOS DO TITANIC")
        print("=" * 40)

        print(f"Total de Passageiros:           {total}")
        print(f"Total de Sobreviventes:         {sobreviventes}")
        print(f"Taxa Geral de Sobrevivência:    {taxa_geral}%")
        print(f"Total de Tarifa Arrecadado:     £ {total_tarifa:,.2f}")
        print(f"Total de Tickets Vendidos:      {tickets_unicos}")

        if not embarque_top.empty:
            local = embarque_top.iloc[0, 0]
            qtd_local = embarque_top.iloc[0, 1]
            print(f"Maior Local de Embarque:        {local} ({qtd_local} pessoas)")

        print("\n" + "-" * 40)
        print("      ESTATÍSTICAS POR SEXO")
        print(sexo_stats.to_string(index=False))

        print("\n" + "-" * 40)
        print("      ESTATÍSTICAS POR CLASSE")
        print(classe_stats.to_string(index=False))

        print("\n" + "-" * 40)
        print("   IDADE E SOBREVIVÊNCIA DE PESSOAS A BORDO")
        print(idade_dist.to_string(index=False))

        print("\n" + "-" * 40)
        print("   SOBREVIVENTES // NÃO SOBREVIVENTES")
        print(status_stats.to_string(index=False))

        # Indicadores para o dashboard
        print("\n" + "-" * 40)
        print("      INDICADORES PARA O DASHBOARD")
        print("-" * 40)

        print(f"KPI 1 - Total de passageiros:        {total}")
        print(f"KPI 2 - Total de sobreviventes:      {sobreviventes}")
        print(f"KPI 3 - Taxa geral de sobrevivência: {taxa_geral}%")
        print(f"KPI 4 - Total de tarifas:            £ {total_tarifa:,.2f}")
        print(f"KPI 5 - Tickets únicos vendidos:     {tickets_unicos}")

        if not embarque_top.empty:
            print(f"KPI 6 - Principal local de embarque: {local}")

        print("Gráficos recomendados:")
        print("- Sobrevivência por sexo")
        print("- Sobrevivência por classe")
        print("- Sobrevivência por faixa etária")
        print("- Sobreviventes vs não sobreviventes")

        # Conclusões escritas
        print("\n" + "-" * 40)
        print("      CONCLUSÕES DA ANÁLISE")
        print("-" * 40)

        print(f"A base analisada possui {total} passageiros.")
        print(f"Foram identificados {sobreviventes} sobreviventes, representando {taxa_geral}% do total.")
        print("Na base utilizada, a sobrevivência por sexo ficou em 100% para mulheres e 0% para homens.")
        print("Esse resultado indica que, neste conjunto de dados específico, todos os sobreviventes registrados são mulheres.")
        print("A primeira classe apresentou a maior taxa de sobrevivência entre as classes analisadas.")
        print("A faixa etária de 60+ apresentou a maior taxa percentual de sobrevivência, embora tenha menor quantidade de registros.")
        print("Os indicadores calculados podem ser usados no dashboard para resumir os principais padrões encontrados.")

        print("=" * 40)

except Exception as e:
    print(f"Ocorreu um erro na análise: {e}")

finally:
    conn.close()

# Fim do script
