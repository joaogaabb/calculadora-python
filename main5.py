"""
ALUGUEL DE CARROS
"""

def alugar_carros(dias, diaria):
    total = dias * diaria
    if dias >= 7:
        total = total * 0.9
    return total

def alugar_motos(dias, diaria):
    total = dias * diaria
    if dias >= 7:
        total = total * 0.9
    return total


def alugar_vans(dias, diaria):
    total = dias * diaria
    if dias >= 7:
        total = total * 0.9
    return total


def aluguel_automoveis():
    while True:
        print("\nSEJA BEM VINDO AO ALUGAUTOMOVEIS")
        print("1 - Alugar carro.")
        print("2 - Alugar moto.")
        print("3 - Alugar van.")
        print("0 - Sair")

        opcao = input("Escolha uma das opções (0/1/2/3): ")

        if opcao == "0":
            print("Saindo do sistema...")
            break


        if opcao not in ["1", "2", "3", "0"]:
            print("Opção inválida.")
            continue

        try:
            dias = int(input("Digite a quantidade de dias: "))
            if dias < 1:
                print("A quantidade de dias deve ser maior que zero.")
                continue

        except ValueError:
            print("Apenas números inteiros.")
            continue


        if opcao == "1":
            print("Alugar carro...")
            resultado = alugar_carros(dias, 150)


        elif opcao == "2":
            print("Alugar moto...")
            resultado = alugar_motos(dias, 90)

        elif opcao == "3":
            print("Alugar van...")
            resultado = alugar_vans(dias, 200)

        print(f"Fica no valor de {resultado:.2f}.")

aluguel_automoveis()