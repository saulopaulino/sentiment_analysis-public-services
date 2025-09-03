import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
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
