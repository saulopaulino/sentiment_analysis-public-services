<<<<<<< HEAD
# sentiment_analysis-public-services
Projeto de Extensão - Centro Universitário UniAméricas
=======
![Capa do Projeto](https://copilot.microsoft.com/th/id/BCO.0ffbf5fb-3767-4c9c-ad40-962e3db42f96.png)

# 📊 Análise de Sentimentos em Reclamações Públicas

Este projeto foi desenvolvido como parte do Projeto de Extensão (PEX) do curso de Ciência de Dados com Ênfase em Inteligência Artificial na Faculdade Descomplica. O objetivo é aplicar técnicas de NLP e IA para analisar sentimentos em reclamações sobre serviços urbanos, como transporte, saúde, segurança e saneamento.

---

### 📂 Dados Utilizados

O arquivo `reclamacoes_simuladas.csv` está localizado na pasta `data/` e contém 100 reclamações públicas simuladas com base em padrões reais. Ele é utilizado para testes e validação dos modelos de análise de sentimentos.


## 🚀 Objetivo

Criar um sistema que:
- Coleta e trata dados de reclamações públicas
- Aplica análise de sentimentos com VADER adaptado ao português
- Exibe os resultados em um dashboard interativo com Streamlit

---

## 🧠 Tecnologias Utilizadas

- **Python**  
- **pandas** – Manipulação de dados  
- **nltk** – Pré-processamento de texto  
- **vaderSentiment** – Análise de sentimentos  
- **streamlit** – Dashboard interativo  
- **plotly** – Gráficos dinâmicos

---

## 📁 Estrutura do Projeto
sentiment-analysis-public-services/ 
├── data/ 
│   └── reclamacoes_simuladas.csv 
│
│── data_colleciton.py
|── preprocessing.py
|── sentiment_analysis.py
|── README.md

---

## ⚙️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/saulopaulino/sentiment_analysis-public-services.git
   cd sentiment_analysis-public-services

2. Instale os pacotes:

pip install -r requirements.txt

3. Execute o pré-processamento:

python src/preprocessing.py

4. Execute a análise de sentimentos:

python src/sentiment_analysis.py

5. Inicie o dashboard:

streamlit run src/dashboard.py

📊 Dashboard
O dashboard exibe:

Gráfico de distribuição de sentimentos

Tabela com reclamações e classificação

Filtro por tipo de sentimento

### 🔗 Acesse o projeto online

Você pode visualizar o projeto rodando em tempo real aqui:  
👉 [Streamlit App](https://sentimentanalysis-public-services.streamlit.app/)


🌍 Impacto Social
Este projeto contribui para a escuta ativa da população e pode ser utilizado por prefeituras, ONGs e startups voltadas para cidades inteligentes. Ele transforma dados não estruturados em insights úteis para a gestão pública.

👨‍💻 Autor
Saulo Paulino Estudante de Ciência de Dados com Ênfase em Inteligência Artificial Faculdade Descomplica Matrícula: 2332124

📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.


---
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)



>>>>>>> 1f4199e (Commit inicial do projeto de análise de sentimentos)
