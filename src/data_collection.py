import pandas as pd
import random

# Reclamações simuladas
reclamacoes = [
    "A iluminação pública está apagada há semanas.",
    "O lixo não foi recolhido na minha rua.",
    "Buracos na pista estão causando acidentes.",
    "Falta de segurança no bairro.",
    "O transporte público está sempre lotado.",
    "Demora no atendimento da saúde pública.",
    "Água com cheiro estranho saindo da torneira.",
    "Barulho excessivo durante a madrugada.",
    "Fila enorme no posto de vacinação.",
    "Problemas com esgoto a céu aberto."
]

# Categorias simuladas
categorias = [
    "Iluminação", "Limpeza Urbana", "Infraestrutura", "Segurança",
    "Transporte", "Saúde", "Saneamento", "Perturbação", "Saúde", "Saneamento"
]

# Gerar DataFrame
df = pd.DataFrame({
    "id": range(1, len(reclamacoes) + 1),
    "texto": reclamacoes,
    "categoria": categorias,
    "regiao": [random.choice(["Zona Norte", "Zona Sul", "Zona Oeste", "Centro"]) for _ in reclamacoes]
})

# Salvar em CSV
df.to_csv("data/complaints.csv", index=False)
print("Arquivo complaints.csv gerado com sucesso!")
