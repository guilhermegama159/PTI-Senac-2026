<div align="center">

# 🚢 Projeto Integrador
### Análise Exploratória de Dados — Titanic
**PI Senado 2026**

</div>

---

## 📌 Visão Geral

Este repositório contém o desenvolvimento do **Projeto Integrador**, que consiste na realização de uma **Análise Exploratória de Dados (EDA)** utilizando o dataset Titanic.

O projeto tem como finalidade aplicar conceitos fundamentais de análise de dados, incluindo organização de projetos, tratamento de dados, análise estatística, visualização de informações e construção de dashboard.

> [!NOTE]
> O projeto é desenvolvido de forma colaborativa utilizando o **GitHub** para controle de versões, estrutura e organização das atividades.

---

## 📖 Introdução

A análise de dados constitui um dos pilares fundamentais da tecnologia, aquirindo conhecimento relevante a partir de grandes volumes brutos de informação estruturada e não estruturada. No contexto educacional, o dataset Titanic  utilizado por reunir dados reais, acessíveis e suficientemente  para sustentar investigações significativas acerca dos fatores que determinaram a sobrevivência dos passageiros no naufrágio de 1912.

O presente projeto propõe a aplicação de técnicas de ciência de dados, compreendendo  fundamentos como coleta, limpeza, análise estatística e visualização e com o objetivo de identificar padrões e correlações entre as variáveis disponíveis, contribuindo para a prática do processo analítico e para o desenvolvimento de competências técnicas.

---

## 🎯 Objetivo Geral

Realizar uma análise exploratória dos dados do Titanic com o objetivo de identificar padrões e relações entre as características dos passageiros e suas chances de sobrevivência.

<details>
<summary>📋 Ver objetivos específicos</summary>

- Compreender a estrutura da base de dados
- Organizar e limpar os dados
- Tratar valores ausentes
- Realizar análise estatística descritiva
- Identificar padrões e correlações
- Criar visualizações informativas
- Desenvolver dashboard interativo
- Documentar todas as etapas do projeto

</details>

---

## 📊 Base de Dados

**Fonte:** [Kaggle — Titanic Dataset](https://www.kaggle.com/datasets/brendan45774/test-file)

| Variável | Tipo | Descrição |
|----------|------|-----------|
| `PassengerId` | int | Identificação do passageiro |
| `Survived` | int | 0 = Não sobreviveu · 1 = Sobreviveu |
| `Pclass` | int | Classe do passageiro (1ª, 2ª ou 3ª) |
| `Name` | str | Nome completo |
| `Sex` | str | Sexo |
| `Age` | float | Idade em anos |
| `SibSp` | int | Número de irmãos ou cônjuges a bordo |
| `Parch` | int | Número de pais ou filhos a bordo |
| `Ticket` | int | Número do bilhete |
| `Fare` | float | Tarifa paga pela passagem |
| `Cabin` | str | Número da cabine |
| `Embarked` | str | Porto de embarque |

---

## 🔄 Preparação dos Dados

> [!IMPORTANT]
> A preparação dos dados constitui etapa fundamental para garantir a integridade e a confiabilidade das análises subsequentes. O pipeline percorre três fases: leitura, tratamento e carga.

### Fluxo de Pipeline

```
CSV bruto (titanic.csv) → Leitura (Pandas) → Inspeção → Tratamento → CSV tratado → SQLite
```

---

<details>
<summary>📂 Etapa 1 — Leitura e inspeção do dataset bruto</summary>

O arquivo `titanic.csv` foi importado por meio da biblioteca **Pandas**. A inspeção inicial revelou um conjunto de **418 registros distribuídos em 12 variáveis**, com os seguintes problemas de integridade:

| Variável | Valores Ausentes | Representatividade |
|----------|-----------------|-------------------|
| `Age` (Idade) | 86 | ~21% dos registros |
| `Cabin` (Cabine) | 327 | ~78% dos registros |
| `Fare` (Tarifa) | 1 | <1% dos registros |

```python
import pandas as pd

df = pd.read_csv('dados/titanic.csv')
print(df.shape)        # (418, 12)
print(df.isnull().sum())
```

Valores ausentes na variável `Cabin` indicou a necessidade de tratamento específico, uma vez que sua eliminação comprometeria a estrutura do dataset.

</details>

---

<details>
<summary>🧹 Etapa 2 — Tratamento, limpeza e padronização</summary>

Com base nos problemas identificados na etapa anterior, foram aplicadas as seguintes transformações:

**1. Renomeação e tradução das colunas**

Todas as variáveis foram renomeadas para o português, promovendo padronização e acessibilidade ao projeto:

```python
df.rename(columns={
    'PassengerId': 'ID',       'Survived': 'Sobreviveu',
    'Pclass':      'Classe',   'Name':     'Nome',
    'Sex':         'Sexo',     'Age':      'Idade',
    'Ticket':      'Ticket',   'Fare':     'Tarifa',
    'Cabin':       'Cabine',   'Embarked': 'Local_Embarque'
}, inplace=True)
```

**2. Tratamento de valores ausentes**

Adotou-se como critério de imputação para variáveis numéricas, por ser uma medida robusta à presença de outliers. Para a variável categórica `Cabine`, optou-se pelo preenchimento com o rótulo `Desconhecido`, preservando o registro sem distorcer distribuições:

```python
df['Idade'].fillna(27.0)            # mediana = 27 anos
df['Tarifa'].fillna(14.45)          # mediana = £14.45
df['Cabine'].fillna('Desconhecido')
```

**3. Conversão de variáveis categóricas**

As variáveis `Classe` e `Local_Embarque` foram convertidas de códigos numéricos e siglas para valores textuais descritivos, facilitando a interpretação nas etapas de visualização:

```python
classe_map   = {1: 'Primeira', 2: 'Segunda', 3: 'Terceira'}
embarque_map = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}

df['Classe']         = df['Classe'].map(classe_map)
df['Local_Embarque'] = df['Local_Embarque'].map(embarque_map)
```

**4. Remoção de variáveis fora do escopo**

As colunas `SibSp` e `Parch` foram excluídas por não integrarem as análises definidas no escopo deste projeto, reduzindo a dimensionalidade do dataset sem perda de informação relevante:

```python
df.drop(columns=['SibSp', 'Parch'], inplace=True)
df.to_csv('dados/titanic_tratado.csv', index=False)
# Resultado: 418 registros · 10 variáveis · 0 valores ausentes
```

</details>

---

<details>
<summary>🗄️ Etapa 3 — Banco de dados SQLite</summary>

O dataset tratado foi inserido em um banco de dados **SQLite** (`dados/titanic.db`), sistema com integração nativa ao Python. Essa abordagem executa consultas SQL nas etapas de análise e alimentação do dashboard, além de garantir a separação entre os dados brutos e os dados prontos para uso:

```python
import sqlite3

conn = sqlite3.connect('dados/titanic.db')
df.to_sql('passageiros', conn, if_exists='replace', index=False)
conn.close()
```

O banco fica armazenado em:

```text
dados/titanic.db
```

</details>

---

### Comparativo: Dataset Bruto × Dataset Tratado

| Atributo | `titanic.csv` (bruto) | `titanic_tratado.csv` (tratado) |
|----------|----------------------|--------------------------------|
| Registros | 418 | 418 |
| Variáveis | 12 | 10 |
| Valores ausentes | 414 (em 3 colunas) | 0 |
| Idioma das colunas | Inglês | Português |
| Variável `Classe` | Numérica (1, 2, 3) | Textual (Primeira, Segunda, Terceira) |
| Variável `Embarque` | Sigla (S, C, Q) | Nome completo do porto |
| Colunas removidas | — | `SibSp`, `Parch` |

---

## 📈 Análises e Transformações Previstas

<details>
<summary> Ver análises planejadas</summary>

- Taxa de sobrevivência por classe
- Taxa de sobrevivência por sexo
- Média de idade por classe e por situação de sobrevivência
- Distribuição da tarifa paga por classe
- Comparação entre sobreviventes e não sobreviventes
- Distribuição etária dos passageiros

</details>

---

## 🔍 Módulo de Análise — `analise.py`

O script conecta-se ao banco `titanic.db` via SQLite e executa consultas SQL para extrair KPIs e análises cruzadas diretamente sobre os dados tratados.
> Este módulo serve de camada intermediária entre o banco de dados e o dashboard, entregando os indicadores já calculados e prontos para visualização.

<details>
<summary>📋 Indicadores extraídos (KPIs)</summary>

| KPI | Descrição |
|-----|-----------|
| Total de passageiros | Contagem geral de registros |
| Total de sobreviventes | Registros com `Sobreviveu = 1` |
| Taxa geral de sobrevivência | Proporção percentual |
| Total de tarifas arrecadadas | Soma da coluna `Tarifa` |
| Tickets únicos vendidos | Contagem distinta de bilhetes |
| Principal porto de embarque | Local com maior frequência |

</details>

<details>
<summary>📊 Análises Cruzadas </summary>

- **Por sexo** — taxa de sobrevivência segmentada entre homens e mulheres
- **Por classe** — comparativo entre Primeira, Segunda e Terceira classe
- **Por faixa etária** — grupos: 0–17 anos, 18–59 anos e 60+ anos
- **Sobreviventes vs. não sobreviventes** — distribuição percentual geral

</details>

<details>
<summary>📌 Conclusão da Análise </summary>

**Todos os sobreviventes registrados são do sexo feminino**, resultando em 100% de sobrevivência para mulheres e 0% para homens um reflexo do protocolo histórico adotado no naufrágio. A **primeira classe** apresentou a maior taxa de sobrevivência entre as classes.

A **faixa etária acima de 60 anos** registrou o maior percentual proporcional de sobrevivência, embora represente o menor grupo em volume absoluto.

</details>

---

## 📊 Dashboard

O dashboard será desenvolvido com **Streamlit** ou biblioteca equivalente, apresentando:
A interface permite filtragem dinâmica por sexo, classe e faixa etária, atualizando em tempo real os indicadores e visualizações.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://titanicdashboardsenac.streamlit.app/)

<div align="center">
  <img src="imagens/Dashboard.gif" alt="Preview do Dashboard Titanic" width="800"/>
</div>

### Funcionalidades disponíveis

| Recurso | Descrição |
|---------|-----------|
| KPIs dinâmicos | Total de passageiros, sobreviventes, taxa de sobrevivência e idade média — todos atualizados conforme os filtros |
| Aba Sobrevivência | Gráfico de barras e grafico em Pizza para visualização por sexo e o geral de sobreviventes |
| Aba Demografia | Histograma de distribuição etária e taxa de sobrevivência por faixa etária |
| Aba Classes | Comparativo de taxa de sobrevivência entre 1ª, 2ª e 3ª classe |
| Aba Estatísticas Detalhadas | Tabelas com highlight dos maiores valores por sexo, classe e faixa etária |

### Como usar o dashboard

1. Acesse o painel lateral esquerdo (**sidebar**)
2. Utilize os filtros **Sexo**, **Classe** e **Faixa Etária** para segmentar os dados
3. Os KPIs no topo da página atualizam automaticamente conforme os filtros aplicados
4. Navegue pelas abas para alternar entre as análises disponíveis
5. Expanda a seção **Conclusões e Insights** ao final da página para ver as principais descobertas

---

## ⚙️ Como Executar o Projeto via Linha de Comando / Pré-requisitos

### Passo 1 — Instale as dependências

```bash
pip install -r requirements.txt
```

### Passo 2 — Execute o pipeline de dados (na ordem)

```bash
python src/tratar_dados.py    # Lê titanic.csv e gera titanic_tratado.csv
python src/salvar_sqlite.py   # Lê titanic_tratado.csv e gera titanic.db
python src/analise.py         # Exibe KPIs e análises no terminal
python src/graficos.py        # Gera os gráficos na pasta /imagens
```

> [!IMPORTANT]
> Os scripts devem ser executados a partir da **raiz do repositório** e na ordem indicada acima, pois cada etapa depende do arquivo gerado pela anterior.

### Passo 4 — Inicie o dashboard

```bash
streamlit run dashboard/app.py
```

O dashboard abrirá automaticamente no navegador em `http://localhost:8501`.

---

## 🧱 Estrutura do Projeto

```text
PTI-Senado-2026/
├── dados/
│   ├── titanic.csv
│   ├── titanic_tratado.csv
│   └── titanic.db
├── notebooks/
│   └── analise.ipynb
├── src/
│   ├── tratar_dados.py
│   ├── salvar_sqlite.py
│   ├── analise.py
│   └── graficos.py
├── dashboard/
│   └── app.py
├── imagens/
├── requirements.txt
└── README.md
```

---

## 🛠️ Metodologia
 
> [!TIP]
> O projeto é estruturado em seis etapas sequenciais. As três primeiras — organização, preparação e transformação dos dados que formam a base analítica do trabalho e são detalhadas a seguir.
>
> **Etapa 1 · Organização** — criação do repositório, definição da estrutura de pastas e inserção dos contribuidores no GitHub.
>
> **Etapa 2 · Preparação dos Dados** — importação do dataset, verificação de inconsistências, tratamento de valores ausentes e padronização das variáveis.
>
> **Etapa 3 · Transformação dos Dados** — conversão de tipos, agrupamentos, filtragens e criação de variáveis derivadas, tais como taxa de sobrevivência por classe e por sexo, e média de idade por classe.
>
> **Etapas 4–6** — banco de dados SQLite, visualizações, dashboard interativo e documentação final.

---

## 👥 Integrantes

O projeto é composto por:

- Rebeca Brandão Vieira
- Victor Cabral
- Dayane Cantão Azarias
- Fabiana Costa dos Santos
- Guilherme de Melo Gama
- Gustavo Duque Ferreira
- Bruno Lira Soares
- Ranieri Portinari Bezerra dos Santos

> Durante o desenvolvimento do projeto, espera-se que os integrantes fortaleçam habilidades de **trabalho em equipe**, **organização de projetos**, **programação** em Python, **análise de dados** e **visualização de informações**.

---

## 💻 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.x-3572A5?style=flat&logo=python&logoColor=white)

![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Graphs-orange)
![NumPy](https://img.shields.io/badge/NumPy-Numerical-013243?style=flat&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat&logo=sqlite&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-181717?style=flat&logo=github&logoColor=white)

> Linguagem utilizada Python, abaixo se encontra as Bibliotecas e Ferramentas.


---

## 📅 Cronograma

| Etapa | Descrição | Responsáveis |
|-------|-----------|--------------|
| 1 | Organização do projeto | Dayane |
| 2 | Preparação dos dados | Victor |
| 3 | Análise dos dados | Ranieri e Fabiana |
| 4 | Banco de dados | Gustavo |
| 4 | Visualização | Rebeca |
| 5 | Dashboard | Guilherme |
| 6 | Documentação | Bruno |

> [!NOTE]
> Todos os integrantes colaboraram de forma conjunta em cada etapa ao longo do desenvolvimento do projeto. Espera-se um dashboard funcional com dados organizados, análises completas, visualizações claras e documentação adequada.

---

 
## 📌 Conclusão

O projeto demonstrou que a análise exploratória de dados coletando padrões significativos a partir de conjuntos de dados reais. 

A partir da aplicação de um pipeline estruturado foi possível identificar que fatores socioeconômicos e demográficos exerceram influência direta sobre as chances de sobrevivência dos passageiros do Titanic. A análise evidenciou que passageiros do sexo feminino, pertencentes à Primeira Classe e situados nas faixas etárias extremas apresentaram as maiores taxas de sobrevivência, corroborando padrões historicamente documentados sobre o naufrágio de 1912.

O dashboard resolve a dificuldade de interpretação de dados históricos brutos, ocasionados pelas limitações de sua época na qual essas mesmas informações sobre os passageiros do Titanic estariam disponíveis apenas em formato tabular, exigindo conhecimento técnico para qualquer análise. Para qualquer usuário independentemente de seu nível de familiaridade com dados conseguiria explorar interativamente os padrões de sobrevivência, e ainda aplicar filtros por sexo, classe e faixa etária, assim obtendo respostas  imediatas, essa acessibilidade transforma dados técnicos em informação compreensível, cumprindo o papel central de qualquer solução de visualização de dados com aplicabilidade direta em contextos educacionais e profissionais.


---

<div align="center">
  <sub>Desenvolvido pelo Grupo 02 - Senac PI Dataset Titanic 2026</sub>
</div>
