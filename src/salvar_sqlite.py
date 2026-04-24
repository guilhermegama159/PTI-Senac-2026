import pandas as pd
import sqlite3

df = pd.read_csv("dados/titanic_tratado.csv")
conn = sqlite3.connect("dados/titanic.db")

df.to_sql("titanic", conn, if_exists="replace", index=False)

teste = pd.read_sql("SELECT * FROM titanic LIMIT 5", conn)
print(teste)

conn.close()

print("Banco SQLite criado com sucesso!")
