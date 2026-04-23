# Arquivo responsável pelo tratamento dos dados do projeto Titanic
"""
Script responsável pelo tratamento  dos dados do arquivo titanic.csv

O tratamento de dados será feito da seguinte maneira:
Remoção de Dados:
- SibSp
- Parch
Nulos: 
- Age (idade): será usado a mediana e transformado em data tipo int
- Fare (tarifa): será usado a mediana 
- Cabin (cabine): será identificado como "Desconhecido"
Padronização:
- Name (nome): será removido as ["] desnecessárias 
- Sex (sexo): Homem ou Mulher 
- Embarked (embarque): em maiúsculo e nome completo, substituindo abreviações (C = Cherbourg Q = Queenstown S = Southampton)
- Pclass (classe do passageiro): será substituido por primeira, segunda e terceira

"""


import pandas as pd


DEBUG = False

df: object = pd.read_csv(r'PTI-Senac-2026\dados\titanic.csv') #df == dataframe
df_tratado: object = df.copy() #Cria uma cópia do df


#Deleta colunas
df_tratado.drop('SibSp', axis=1, inplace=True)
df_tratado.drop('Parch', axis=1, inplace=True)

#Renomeando colunas para o português
df_tratado.columns = ['ID','Sobreviveu','Classe','Nome','Sexo','Idade','Ticket','Tarifa','Cabine','Local_Embarque']

#Criação de variáveis para valores padrão
idade_mediana: float = df['Age'].median()

tarifa_mediana: float = df['Fare'].median()

locais_de_embarque: dict = {'C': 'Cherbourg',
                            'Q': 'Queenstown',
                            'S': 'Southampton'}

sexo: dict = {'male': 'Homem',
              'female': 'Mulher'}

classe_passageiro = {1: 'Primeira',
                     2: 'Segunda',
                     3: 'Terceira'}

#Preenchimento de valores nulos
df_tratado['Idade'] = df_tratado['Idade'].fillna(idade_mediana, inplace=True)
df_tratado['Tarifa'] = df_tratado['Tarifa'].fillna(tarifa_mediana, inplace=True)
df_tratado['Cabine'] = df_tratado['Cabine'].fillna('Desconhecido', inplace=True)

#Transformação de dados
df_tratado['Nome'] = df_tratado['Nome'].str.replace(r'["]+', '', regex=True)
df_tratado['Nome'] = df_tratado['Nome'].astype(str)

df_tratado['Classe'] = df_tratado['Classe'].replace(classe_passageiro)
df_tratado['Classe'] = df_tratado['Classe'].astype(str)

df_tratado['Idade'] = df_tratado['Idade'].astype(int)

df_tratado['Local_Embarque'] = df_tratado['Local_Embarque'].replace(locais_de_embarque)

df_tratado['Sexo'] = df_tratado['Sexo'].replace(sexo)


#Apenas salva o novo arquivo se DEBUG = False
assert DEBUG == False, 'Script rodando em modo de debug.\nArquivo não será salvo'
df_tratado.to_csv(r'PTI-Senac-2026\dados\titanic_tratado.csv', index=False)
