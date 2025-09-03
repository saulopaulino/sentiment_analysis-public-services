import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Inicializar o analisador
analyzer = SentimentIntensityAnalyzer()

# Carregar dados limpos
df = pd.read_csv("data/complaints_clean.csv")

# Função para analisar sentimento
def analisar_sentimento(texto):
    resultado = analyzer.polarity_scores(texto)
    polaridade = resultado['compound']
    if polaridade >= 0.05:
        return "positivo"
    elif polaridade <= -0.05:
        return "negativo"
    else:
        return "neutro"

portuguese_lexicon = {
    "excelente": 3.0,
    "ótimo": 2.5,
    "bom": 2.0,
    "regular": 0.5,
    "ruim": -2.0,
    "péssimo": -3.0,
    "atraso": -2.5,
    "resolvido": 1.5,
    "cancelado": -2.0,
    "inaceitável": -3.0,
    "ajuda": 1.8,
    "problema": -2.2,
    "reembolso": 1.0,
    "demora": -2.0,
    "satisfeito": 2.2,
    "insatisfeito": -2.5
}

analyzer.lexicon.update(portuguese_lexicon)


# Aplicar análise
df["sentimento"] = df["texto_final"].apply(analisar_sentimento)

# Salvar resultados
df.to_csv("data/complaints_sentiment.csv", index=False)
print("Análise de sentimentos com VADER concluída. Arquivo complaints_sentiment.csv gerado!")
