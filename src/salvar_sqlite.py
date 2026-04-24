import pandas as pd
import sqlite3

df = pd.read_csv("dados/titanic_tratado.csv")

conn = sqlite3.connect("dados/titanic.db")

df.to_sql("passageiros", conn, if_exists="replace", index=False)

conn.close()

print("Banco de dados criado com sucesso em dados/titanic.db")
