"""
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

resultado = num1 + (num2 * num3)

print(f"O resultado é {resultado}")

"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def potencia(a, b):
    if a == 0 and b < 0:
        return "Erro; Zero elevado a expoente negativo"
    return a ** b

def calculadora():
    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Potencia")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrendo calculadora")
            break

        if opcao not in ("1", "2", "3", "4", "5", "0"):
            print("Opção inválida")
            continue

        try:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
        except ValueError:
            print("Digite apenas números")
            continue

        if opcao == "1":
            resultado = somar(num1, num2)

        elif opcao == "2":
            resultado = subtrair(num1, num2)

        elif opcao == "3":
            resultado = multiplicar(num1, num2)

        elif opcao == "4":
            resultado = dividir(num1, num2)

        else:
            resultado = potencia(num1, num2)

        print(f"Resultado: {resultado}")

calculadora()








