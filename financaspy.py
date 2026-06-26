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

# Menu

while True:
    print("\n--- MENU ---")
    print("1 - REGISTRAR")
    print("2 - VER EXTRATO")
    print("3 - RELATÓRIO")
    print("4 - EXPORTAR")
    print("5 - SAIR")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- REGISTRAR ---")
        tipo = input("Tipo (Receita/Despesa): ").strip().capitalize()