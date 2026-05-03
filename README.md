# 🚢 Projeto Integrador  
## Análise Exploratória de Dados - Titanic

---

## 📌 Visão Geral

Este repositório contém o desenvolvimento do **Projeto Integrador**, que consiste na realização de uma **Análise Exploratória de Dados (EDA)** utilizando o dataset Titanic.

O projeto tem como finalidade aplicar conceitos fundamentais de análise de dados, incluindo:

- Organização de projetos  
- Tratamento de dados  
- Análise estatística  
- Visualização de informações  
- Construção de dashboard  

O projeto será desenvolvido de forma colaborativa utilizando o **GitHub** para controle de versões e organização das atividades.

---

## 📖 Introdução

A análise de dados é uma área fundamental da tecnologia moderna, permitindo extrair informações relevantes a partir de grandes conjuntos de dados.

O dataset Titanic é amplamente utilizado em projetos educacionais por possuir dados reais e permitir análises significativas sobre fatores que influenciaram a sobrevivência dos passageiros.

Este projeto busca aplicar técnicas básicas de ciência de dados para compreender melhor esses fatores.

---

## 🎯 Objetivo Geral

Realizar uma análise exploratória dos dados do Titanic com o objetivo de identificar padrões e relações entre as características dos passageiros e suas chances de sobrevivência.

---

## 🎯 Objetivos Específicos

- Compreender a estrutura da base de dados  
- Organizar os dados  
- Tratar valores ausentes  
- Realizar análise estatística  
- Identificar padrões  
- Criar visualizações  
- Desenvolver dashboard  
- Documentar o projeto  

---

## 📊 Base de Dados

### Dataset Utilizado

O projeto utilizará o dataset Titanic, contendo informações sobre passageiros do navio.

**Fonte:**

https://www.kaggle.com/datasets/brendan45774/test-file

---

### Variáveis Disponíveis

| Variável | Descrição |
|---------|-----------|
| PassengerId | Identificação do passageiro |
| Survived | Situação de sobrevivência |
| Pclass | Classe do passageiro |
| Name | Nome |
| Sex | Sexo |
| Age | Idade |
| SibSp | Número de irmãos ou cônjuges |
| Parch | Número de pais ou filhos |
| Ticket | Número do ticket |
| Fare | Tarifa paga |
| Cabin | Cabine |
| Embarked | Porto de embarque |

---

## 🗄️ Banco de Dados

Os dados serão armazenados em um banco de dados utilizando **SQLite**, um sistema leve integrado ao Python.

Após a importação e tratamento do dataset Titanic, os dados serão armazenados em um banco SQLite para facilitar consultas e análises.

### Benefícios do Banco de Dados

- Armazenamento estruturado  
- Melhor organização das informações  
- Consultas SQL  
- Integração com Python  
- Apoio na geração de gráficos  

---

### Estrutura do Banco

O banco conterá uma tabela com as seguintes colunas:

- PassengerId  
- Survived  
- Pclass  
- Name  
- Sex  
- Age  
- SibSp  
- Parch  
- Ticket  
- Fare  
- Cabin  
- Embarked  

---

### Processo de Armazenamento

1. Importação do arquivo CSV  
2. Limpeza dos dados  
3. Tratamento de valores ausentes  
4. Inserção no SQLite  

---

### Arquivo do Banco

O banco ficará armazenado na seguinte pasta:
```text
dados/titanic.db
```
---

## 👥 Integrantes

O projeto é composto por:

- REBECA BRANDAO VIEIRA  
- VICTOR CABRAL  
- DAYANE CANTÃO AZARIAS  
- FABIANA COSTA DOS SANTOS  
- GUILHERME DE MELO GAMA  
- GUSTAVO DUQUE FERREIRA  
- BRUNO LIRA SOARES  
- RANIERI PORTINARI BEZERRA DOS SANTOS  

---

## 🛠️ Metodologia

O projeto seguirá as seguintes etapas:

### 1 — Organização

- Criação do repositório  
- Definição da estrutura  
- Inserção dos colaboradores  

---

### 2 — Preparação dos Dados

- Importação do dataset  
- Verificação de inconsistências  
- Tratamento de valores ausentes  
- Padronização  

---

### 3 — Transformação dos Dados

Transformações previstas:

- Conversão de tipos  
- Agrupamentos  
- Filtragens  
- Variáveis derivadas  

#### Exemplos:

- Taxa de sobrevivência por classe  
- Taxa de sobrevivência por sexo  
- Média de idade por classe  

---

### 4 — Análise de Dados

Serão realizadas análises como:

- Médias  
- Proporções  
- Comparações  
- Distribuições  

---

### 5 — Visualização de Dados

Serão criados gráficos para facilitar a interpretação.

---

### 6 — Desenvolvimento do Dashboard

Será criado um dashboard interativo com as principais informações.

---

### 7 — Documentação

Serão registradas todas as etapas do projeto.

---

## 📈 Transformações Previstas

### Limpeza

- Remoção de dados inconsistentes  
- Tratamento de valores nulos  
- Ajuste de colunas  

---

### Organização

- Renomeação de colunas  
- Padronização  
- Separação de dados  

---

### Cálculos

- Taxas  
- Médias  
- Percentuais  

---

## 📊 Dashboard

### Objetivo

Apresentar os dados de forma visual e intuitiva.

---

### Visualizações Previstas

- Sobrevivência por sexo  
- Sobrevivência por classe  
- Distribuição de idade  
- Comparação entre sobreviventes e não sobreviventes  
- Outras análises relevantes  

---

### Indicadores

O dashboard apresentará:

- Total de passageiros  
- Total de sobreviventes  
- Taxa de sobrevivência  
- Idade média  

---


## 🧱 Estrutura do Projeto

```text
Projeto-Titanic
PI-Senac-2026/
├── dados/
│   └── titanic.csv
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

## 💻 Tecnologias Utilizadas

### Linguagem

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

---

### Bibliotecas

![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)

![Matplotlib](https://img.shields.io/badge/Matplotlib-Graphs-orange)

![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?logo=numpy)

---

### Ferramentas

![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)

![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)

---

## 📅 Cronograma

| Etapa | Descrição | Responsáveis |
|------|-----------|--------------|
| 1 | Organização do projeto | Dayane |
| 2 | Preparação dos dados | Victor |
| 3 | Análise dos dados | Ranieri e Fabiana |
| 4 | Banco de dados | Gustavo |
| 4 | Visualização | Rebeca |
| 5 | Dashboard | Guilherme |
| 6 | Documentação | Bruno |

Todos os integrantes colaborarão de forma conjunta em cada etapa ao longo do desenvolvimento do projeto.

---

## 📊 Resultados Esperados

Ao final do projeto espera-se:

- Dashboard funcional  
- Dados organizados  
- Análises completas  
- Visualizações claras  
- Documentação adequada  

---

## 📚 Aprendizados Esperados

Durante o projeto serão desenvolvidas habilidades como:

- Trabalho em equipe  
- Organização de projetos  
- Programação  
- Análise de dados  
- Visualização de dados  

---

## 📌 Conclusão

Este projeto representa a aplicação prática dos conhecimentos adquiridos.

A análise do dataset Titanic permitirá compreender como a análise de dados pode ser utilizada para extrair informações relevantes a partir de dados reais.

O desenvolvimento do projeto contribuirá para o aprendizado técnico e para o desenvolvimento de habilidades práticas na área de tecnologia.
