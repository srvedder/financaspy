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


        try:
            valor = float(input("Valor: ").replace(",", "."))
        except ValueError:
            print("Valor inválido! Registro cancelado.")
            continue

        categoria = input("Categoria: ").strip().capitalize()
        descricao = input("Descrição: ").strip()
        data = "Hoje"


        lancamento = {"data": data, "tipo": tipo, "valor": valor, "categoria": categoria, "descricao": descricao}
        historico.append(lancamento)


        with open(ARQUIVO, "a", encoding="utf-8") as f:
            f.write(f"{data} | {tipo} | {valor} | {categoria} | {descricao}\n")
        print("Registrado e salvo com sucesso!")

        print("\n--- EXTRATO ---")
        if not historico:
            print("Nenhum lançamento.")
        for l in historico:
            print(f"{l['data']} - {l['tipo']} - {l['categoria']}: R$ {l['valor']:.2f} ({l['descricao']})")

    elif opcao == "3":
        print("\n--- RELATÓRIO ---")
        total_receitas = 0
        total_despesas = 0
        por_categoria = {}

        for l in historico:
            if l["tipo"] == "Receita":
                total_receitas += l["valor"]
                por_categoria[l["categoria"]] = por_categoria.get(l["categoria"], 0) + l["valor"]
            elif l["tipo"] == "Despesa":
                total_despesas += l["valor"]
                por_categoria[l["categoria"]] = por_categoria.get(l["categoria"], 0) - l["valor"]

        saldo_total = total_receitas - total_despesas

        print(f"Total Receitas: R$ {total_receitas:.2f}")
        print(f"Total Despesas: R$ {total_despesas:.2f}")
        print(f"Saldo Total: R$ {saldo_total:.2f}")
        print("Por Categoria:")
        for cat, val in por_categoria.items():
            print(f"  {cat}: R$ {val:.2f}")

    elif opcao == "4":
        # Gera o relatorio.txt
        total_receitas = sum(l["valor"] for l in historico if l["tipo"] == "Receita")
        total_despesas = sum(l["valor"] for l in historico if l["tipo"] == "Despesa")

        por_categoria = {}
        for l in historico:
            ajuste = l["valor"] if l["tipo"] == "Receita" else -l["valor"]
            por_categoria[l["categoria"]] = por_categoria.get(l["categoria"], 0) + ajuste

        with open("relatorio.txt", "w", encoding="utf-8") as f:
            f.write("=== RELATÓRIO FINANCEIRO ===\n")
            f.write(f"Total Receitas: R$ {total_receitas:.2f}\n")
            f.write(f"Total Despesas: R$ {total_despesas:.2f}\n")
            f.write(f"Saldo Total: R$ {total_receitas - total_despesas:.2f}\n\n")
            f.write("Por Categoria:\n")
            for cat, val in por_categoria.items():
                f.write(f"  {cat}: R$ {val:.2f}\n")
        print("\nArquivo 'relatorio.txt' gerado!")

    elif opcao == "5":
        print("Saindo... Dados salvos automaticamente.")
        break
    else:
        print("Opção inválida!")