import pandas as pd
import sqlite3

conn = sqlite3.connect("dados/titanic.db")

df = pd.read_csv('dados/titanic_tratado.csv')

df.to_sql('passageiros', conn, if_exists='replace', index=False)

conn.close()

print("Banco SQLite criado com sucesso!")
