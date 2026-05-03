import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
import os

# imagem titanic
st.markdown("""
<style>
.hero {
    position: relative;
    height: 300px;
    background: 
        linear-gradient(rgba(15,23,42,0.7), rgba(15,23,42,0.9)),
        url("https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg");
    background-size: cover;
    background-position: center;
    border-radius: 12px;
    margin-bottom: 20px;
}

.hero-content {
    position: absolute;
    bottom: 30px;
    left: 40px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# titulo
st.markdown("""
<div class="hero">
    <div class="hero-content">
        <h1>Dashboard Titanic</h1>
        <p>Análise de sobrevivência interativo</p>
    </div>
</div>
""", unsafe_allow_html=True)

if "fechar_aviso" not in st.session_state:
    st.session_state.fechar_aviso = False

if not st.session_state.fechar_aviso:
    col1, col2 = st.columns([10, 1])

    with col1:
        st.markdown("""
        <div style="
            background: #1e293b;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #38bdf8;
            margin-bottom: 1rem;
            font-size: 0.95rem;
        ">
            💡 Para melhor visualização dos dados, recomendamos o uso do modo escuro.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if st.button("❌ Fechar aviso", use_container_width=True):
            st.session_state.fechar_aviso = True

#estilo
st.markdown("""
<style>
    /* Fundo geral */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: #e2e8f0;
        padding: 2rem 3rem;
    }

    /* Cards de metricas */
    .metric-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 1rem;
        margin: 0.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.05);
        transition: 0.3s;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 25px rgba(0,0,0,0.6);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #020617;
        border-right: 1px solid #1e293b;
    }

    .sidebar-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #38bdf8;
        margin-bottom: 1rem;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        background-color: #3C7A89;
        border-radius: 8px;
        padding: 10px;
        margin-right: 5px;
        margin-top: 1rem;
    }

    .stTabs [aria-selected="true"] {
        background: #3C7A99 !important;
        color: white !important;
        margin-top: 1rem;
    }
    
    .block-container {
    max-width: 1200px;
    margin: auto;
    }

    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #38bdf8, transparent);
    }
</style>
""", unsafe_allow_html=True)

st.divider()

#conectar com banco
caminho_csv = os.path.join(os.path.dirname(__file__), "..", "dados", "titanic_tratado.csv")
df = pd.read_csv(caminho_csv)

#padronizar nomes de colunas
df.columns = df.columns.str.strip()

#tratamento de dados
if "Idade" in df.columns:
    df["Idade"] = df["Idade"].fillna(df["Idade"].median())

#funcao classificar idade
def classificar_idade(idade):
    if pd.isna(idade):
        return "Não Informada"
    elif idade < 18:
        return "0-17 anos"
    elif idade <= 59:
        return "18-59 anos"
    else:
        return "60+ anos"

if "Idade" in df.columns:
    df["faixa_etaria"] = df["Idade"].apply(classificar_idade)

st.sidebar.markdown('<p class="sidebar-header">🎛️ Filtros Interativos</p>', unsafe_allow_html=True)

df_filtrado = df.copy()

#filtro sexo
if "Sexo" in df.columns:
    opcoes_sexo = ["Todos"] + sorted(df["Sexo"].dropna().unique().tolist())
    sexo = st.sidebar.selectbox("Filtrar por Sexo", opcoes_sexo)

    if sexo != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Sexo"] == sexo]

#filtro classe
if "Classe" in df.columns:
    opcoes_classe = ["Todas"] + sorted(df["Classe"].dropna().unique().tolist())
    classe = st.sidebar.selectbox("Filtrar por Classe", opcoes_classe)

    if classe != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Classe"] == classe]

#filtro faixa etaria
if "faixa_etaria" in df.columns:
    opcoes_faixa = ["Todas"] + sorted(df["faixa_etaria"].dropna().unique().tolist())
    faixa_etaria = st.sidebar.selectbox("Filtrar por Faixa Etária", opcoes_faixa)

    if faixa_etaria != "Todas":
        df_filtrado = df_filtrado[df_filtrado["faixa_etaria"] == faixa_etaria]

#metricas principais
st.subheader("📈 Métricas Principais")

col1, col2, col3, col4 = st.columns(4)

total = len(df_filtrado)
sobreviventes = int(df_filtrado["Sobreviveu"].sum()) if "Sobreviveu" in df_filtrado.columns else 0
taxa = (df_filtrado["Sobreviveu"].mean()*100) if "Sobreviveu" in df_filtrado.columns else 0
idade_media = df_filtrado["Idade"].mean() if "Idade" in df_filtrado.columns else 0

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="margin: 0; color: #1f77b4;">Total de Passageiros</h3>
        <p style="font-size: 2rem; margin: 0.5rem 0; font-weight: bold;">{total:,}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="margin: 0; color: #28a745;">Sobreviventes</h3>
        <p style="font-size: 2rem; margin: 0.5rem 0; font-weight: bold;">{sobreviventes:,}</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="margin: 0; color: #ffc107;">Taxa de Sobrevivência</h3>
        <p style="font-size: 2rem; margin: 0.5rem 0; font-weight: bold;">{taxa:.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="margin: 0; color: #6c757d;">Idade Média</h3>
        <p style="font-size: 2rem; margin: 0.5rem 0; font-weight: bold;">{idade_media:.1f} anos</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

#analisesvisuais
st.subheader("📊 Análises Visuais")

tab1, tab2, tab3, tab4 = st.tabs(["📈 Sobrevivência", "👥 Demografia", "🎫 Classes", "📋 Estatísticas Detalhadas"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        if "Sexo" in df_filtrado.columns and "Sobreviveu" in df_filtrado.columns:
            fig_sex = px.bar(
                df_filtrado.groupby("Sexo")["Sobreviveu"].mean().reset_index(),
                x="Sexo",
                y="Sobreviveu",
                title="Taxa de Sobrevivência por Sexo",
                labels={"Sexo": "Sexo", "Sobreviveu": "Taxa de Sobrevivência"},
                color="Sexo",
                color_discrete_map={"Homem": "#1f77b4", "Mulher": "#ff7f0e"}
            )
            fig_sex.update_layout(yaxis_tickformat='.1%')
            st.plotly_chart(fig_sex, use_container_width=True)

    with col2:
        if "Sobreviveu" in df_filtrado.columns:
            sobreviventes_count = df_filtrado["Sobreviveu"].value_counts()

            labels_map = {
                0: "Não Sobreviveu",
                1: "Sobreviveu"
            }

            nomes = [labels_map.get(i, str(i)) for i in sobreviventes_count.index]

            fig_pie = px.pie(
                values=sobreviventes_count.values,
                names=nomes,
                title="Distribuição de Sobreviventes",
                color=nomes,
                color_discrete_map={
                    "Não Sobreviveu": "#dc3545",
                    "Sobreviveu": "#28a745"
                }
            )

            st.plotly_chart(fig_pie, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        if "Idade" in df_filtrado.columns:
            fig_age = px.histogram(
                df_filtrado,
                x="Idade",
                title="Distribuição de Idade dos Passageiros",
                labels={"Idade": "Idade"},
                nbins=30,
                color_discrete_sequence=["#17a2b8"]
            )
            fig_age.update_layout(bargap=0.1)
            st.plotly_chart(fig_age, use_container_width=True)

    with col2:
        if "faixa_etaria" in df_filtrado.columns and "Sobreviveu" in df_filtrado.columns:
            fig_age_survival = px.bar(
                df_filtrado.groupby("faixa_etaria")["Sobreviveu"].mean().reset_index(),
                x="faixa_etaria",
                y="Sobreviveu",
                title="Taxa de Sobrevivência por Faixa Etária",
                labels={"faixa_etaria": "Faixa Etária", "Sobreviveu": "Taxa de Sobrevivência"},
                color="faixa_etaria",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_age_survival.update_layout(yaxis_tickformat='.1%')
            st.plotly_chart(fig_age_survival, use_container_width=True)

with tab3:
    if "Classe" in df_filtrado.columns and "Sobreviveu" in df_filtrado.columns:
        fig_class = px.bar(
            df_filtrado.groupby("Classe")["Sobreviveu"].mean().reset_index(),
            x="Classe",
            y="Sobreviveu",
            title="Taxa de Sobrevivência por Classe",
            labels={"Classe": "Classe", "Sobreviveu": "Taxa de Sobrevivência"},
            color="Classe",
            color_discrete_sequence=["#ffd700", "#c0c0c0", "#cd7f32"]
        )
        fig_class.update_layout(yaxis_tickformat='.1%')
        st.plotly_chart(fig_class, use_container_width=True)

with tab4:
    st.subheader("📋 Estatísticas Detalhadas")

    if "Sexo" in df_filtrado.columns and "Sobreviveu" in df_filtrado.columns:
        st.write("**Estatísticas por Sexo:**")
        stats_sex = df_filtrado.groupby("Sexo")["Sobreviveu"].agg(["count", "sum", lambda x: x.mean()*100]).round(2)
        stats_sex.columns = ["Total", "Sobreviventes", "Taxa (%)"]
        st.dataframe(stats_sex.style.highlight_max(axis=0, color="#3C7A99"))

    if "Classe" in df_filtrado.columns and "Sobreviveu" in df_filtrado.columns:
        st.write("**Estatísticas por Classe:**")
        stats_class = df_filtrado.groupby("Classe")["Sobreviveu"].agg(["count", "sum", lambda x: x.mean()*100]).round(2)
        stats_class.columns = ["Total", "Sobreviventes", "Taxa (%)"]
        st.dataframe(stats_class.style.highlight_max(axis=0, color='#3C7A99'))

    if "faixa_etaria" in df_filtrado.columns and "Sobreviveu" in df_filtrado.columns:
        st.write("**Estatísticas por Faixa Etária:**")
        stats_age = df_filtrado.groupby("faixa_etaria")["Sobreviveu"].agg(["count", "sum", lambda x: x.mean()*100]).round(2)
        stats_age.columns = ["Total", "Sobreviventes", "Taxa (%)"]
        st.dataframe(stats_age.style.highlight_max(axis=0, color='#3C7A99'))

#conclusoes
st.divider()
st.subheader("🎯 Conclusões e Insights")

with st.expander("📊 Principais Descobertas"):
    st.markdown("""
    - **Diferenças por Sexo**: Mulheres apresentaram taxas de sobrevivência significativamente maiores que homens.
    - **Influência da Classe**: Passageiros de classes superiores tiveram maiores chances de sobrevivência.
    - **Faixa Etária**: Crianças e jovens tiveram melhores taxas, enquanto idosos enfrentaram maiores riscos.
    - **Fatores Combinados**: A combinação de sexo feminino, classe alta e idade jovem maximizava as chances de sobrevivência.
    """)

with st.expander("🔍 Metodologia"):
    st.markdown("""
    - **Fonte de Dados**: Dataset tratado do Titanic com informações de passageiros.
    - **Tratamento**: Valores nulos preenchidos com medianas, categorização por faixas etárias.
    - **Análises**: Foco em correlações entre variáveis demográficas e taxa de sobrevivência.
    - **Ferramentas**: Python (Pandas, Plotly), Streamlit para visualização interativa.
    """)
    
    
    
st.markdown("""
<div style="text-align: center; opacity: 0.6; font-size: 0.85rem;">
Dashboard desenvolvido para análise de dados do Titanic - Projeto PI Senac • Python • Streamlit • 2026
</div>
""", unsafe_allow_html=True)