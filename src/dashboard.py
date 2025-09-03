import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
<<<<<<< HEAD
df = pd.read_csv("data/reclamacoes_simuladas.csv")

# Título
st.title("📊 Análise de Sentimentos em Reclamações")

# Filtros
categoria = st.selectbox("Filtrar por categoria:", df["categoria"].unique())
regiao = st.selectbox("Filtrar por região:", df["regiao"].unique())

df_filtrado = df[(df["categoria"] == categoria) & (df["regiao"] == regiao)]

# Métricas
st.subheader("📌 Indicadores de Sentimento")
col1, col2, col3 = st.columns(3)
col1.metric("Positivas", df_filtrado[df_filtrado["sentimento"] == "positivo"].shape[0])
col2.metric("Negativas", df_filtrado[df_filtrado["sentimento"] == "negativo"].shape[0])
col3.metric("Neutras", df_filtrado[df_filtrado["sentimento"] == "neutro"].shape[0])

# Gráfico de pizza
st.subheader("📈 Distribuição de Sentimentos")
fig = px.pie(df_filtrado, names="sentimento", title="Sentimentos por Reclamações")
st.plotly_chart(fig)

# Tabela com destaque
st.subheader("📋 Reclamações Filtradas")
st.dataframe(df_filtrado.style.applymap(
    lambda x: 'background-color: #d4f4dd' if x == 'positivo' else 
              'background-color: #fdd' if x == 'negativo' else 
              'background-color: #eee' if x == 'neutro' else '',
    subset=['sentimento']
))

# Rodapé
st.markdown("---")
st.caption("Projeto desenvolvido por Saulo Paulino • Faculdade DESCOMPLICA • PEX - Ciência de Dados e IA")
=======
df = pd.read_csv("data/complaints_sentiment.csv")

# Título
st.set_page_config(page_title="Dashboard de Sentimentos", layout="wide")
st.title("📊 Dashboard de Análise de Sentimentos")

# Filtro de sentimento
opcao = st.selectbox("Filtrar por sentimento:", ["todos", "positivo", "negativo", "neutro"])
df_filtrado = df if opcao == "todos" else df[df["sentimento"] == opcao]

# Gráfico interativo
st.subheader("Distribuição de Sentimentos")
contagem = df["sentimento"].value_counts().reset_index()
contagem.columns = ["Sentimento", "Quantidade"]
fig = px.bar(contagem, x="Sentimento", y="Quantidade", color="Sentimento",
             color_discrete_map={"positivo": "green", "negativo": "red", "neutro": "gray"},
             title="Quantidade de Reclamações por Sentimento")
st.plotly_chart(fig, use_container_width=True)

# Tabela com expansão
st.subheader("📋 Reclamações e Sentimentos")
with st.expander("Visualizar dados"):
    st.dataframe(df_filtrado[["texto", "sentimento"]], use_container_width=True)
>>>>>>> 1f4199ea3e4401458342ff8e58a9a79b5ad60001
