import os

ARQUIVO = "historico.txt"
historico = []

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(" | ")
            if len(partes) == 5:
                historico.append({
                    "data": partes[0], "tipo": partes[1],
                    "valor": float(partes[2]), "categoria": partes[3], "descricao": partes[4]
                })
