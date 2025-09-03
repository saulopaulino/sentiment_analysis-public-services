import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar recursos do NLTK (executar uma vez)
nltk.download('punkt')
nltk.download('stopwords')

# Função de limpeza de texto
def limpar_texto(texto):
    texto = texto.lower()  # caixa baixa
    texto = re.sub(r"http\S+", "", texto)  # remover links
    texto = re.sub(r"[^a-zA-Záéíóúãõâêôç ]", "", texto)  # remover pontuação
    texto = re.sub(r"\s+", " ", texto)  # remover espaços extras
    return texto.strip()

# Função para remover stopwords
def remover_stopwords(texto):
    palavras = word_tokenize(texto, language='portuguese')
    stop_words = set(stopwords.words('portuguese'))
    palavras_filtradas = [p for p in palavras if p not in stop_words]
    return " ".join(palavras_filtradas)

# Carregar dados
df = pd.read_csv("data/complaints.csv")

# Aplicar pré-processamento
df["texto_limpo"] = df["texto"].apply(limpar_texto)
df["texto_final"] = df["texto_limpo"].apply(remover_stopwords)

# Salvar novo CSV
df.to_csv("data/complaints_clean.csv", index=False)
print("Pré-processamento concluído. Arquivo complaints_clean.csv gerado!")
