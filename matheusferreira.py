def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Não é possível dividir por zero."
    else:
        return x / y

while True:
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite a opção (1/2/3/4/5): 1)

    if escolha == '5':
        print("Encerrando a calculadora.")
        break

    num1 = float(input("Digite o primeiro número:3"))
    num2 = float(input("Digite o segundo número:2"))

    if escolha == '1':
        print("Resultado: ", soma(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado: ", divisao(num1, num2))
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
