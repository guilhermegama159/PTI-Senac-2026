import pandas as pd
import matplotlib.pyplot as plt
import os

plt.style.use("ggplot")

os.makedirs("imagens", exist_ok=True)

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_atual, "..", "dados", "titanic_tratado.csv")

df = pd.read_csv(caminho_csv)

def adicionar_porcentagem(ax):
    for p in ax.patches:
        altura = p.get_height()
        ax.annotate(f'{altura:.2f}%',
                    (p.get_x() + p.get_width() / 2, altura),
                    ha='center', va='bottom')

def classificar_idade(idade):
    if pd.isna(idade):
        return "Não Informada"
    elif idade < 18:
        return "0-17"
    elif idade <= 59:
        return "18-59"
    else:
        return "60+"

df["Faixa_Etaria"] = df["Idade"].apply(classificar_idade)

plt.figure(figsize=(8,5))

valores = df.groupby("Sexo")["Sobreviveu"].mean() * 100
valores = valores.round(2)

ax = valores.plot(kind="bar", color=["#1f77b4", "#ff7f0e"])

plt.title("Taxa de Sobrevivência por Sexo")
plt.ylabel("Porcentagem (%)")
adicionar_porcentagem(ax)

plt.tight_layout()
plt.savefig("imagens/sobrevivencia_por_sexo.png")
plt.close()

plt.figure(figsize=(8,5))

valores = df.groupby("Classe")["Sobreviveu"].mean() * 100
valores = valores.round(2)

ax = valores.plot(kind="bar", color=["#2ca02c", "#d62728", "#9467bd"])

plt.title("Taxa de Sobrevivência por Classe")
plt.ylabel("Porcentagem (%)")
adicionar_porcentagem(ax)

plt.tight_layout()
plt.savefig("imagens/sobrevivencia_por_classe.png")
plt.close()

plt.figure(figsize=(8,5))

valores = df.groupby("Faixa_Etaria")["Sobreviveu"].mean() * 100
valores = valores.round(2)

ax = valores.plot(kind="bar", color=["#8dd3c7", "#ffffb3", "#bebada"])

plt.title("Taxa de Sobrevivência por Faixa Etária")
plt.ylabel("Porcentagem (%)")
adicionar_porcentagem(ax)

plt.tight_layout()
plt.savefig("imagens/faixa_etaria.png")
plt.close()

plt.figure(figsize=(6,6))

dados = df["Sobreviveu"].value_counts().sort_index()

plt.pie(
    dados,
    labels=["Não Sobreviveu", "Sobreviveu"],
    autopct="%1.2f%%",
    colors=["#ff4d4d", "#66b3ff"],
    startangle=90
)

plt.title("Sobreviventes x Não Sobreviventes")
plt.tight_layout()
plt.savefig("imagens/sobreviventes_vs_nao.png")
plt.close()

print("graficos gerados")

