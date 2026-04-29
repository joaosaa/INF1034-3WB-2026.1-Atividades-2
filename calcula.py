def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print('INDEFINIDO')
    return a / b


def calculadora():
    ultimo_resultado = None

    while True:
        print("Selecione a operação:")
        print("Somar(+)")
        print("Subtrair(-)")
        print("Multiplicar(x)")
        print("Dividir(:)")
        print("sair. Encerrar")

        escolha = input("Digite sua escolha (+/-/:/x/sair): ")

        if escolha == "sair":
            break

        if escolha not in ('+', '-', ':', 'x'):
            print("Escolha inválida!")
            continue

        if ultimo_resultado is not None:
            usar_memoria = input(f"Usar último resultado {ultimo_resultado}? (sim/nao): ")
            if usar_memoria == 'sim':
                a = ultimo_resultado
            else:
                a = float(input("Digite o primeiro número: "))
        else:
            a = float(input("Digite o primeiro número: "))

        b = float(input("Digite o segundo número: "))

        if escolha == '+':
            resultado = somar(a, b)
        elif escolha == '-':
            resultado = subtrair(a, b)
        elif escolha == 'x':
            resultado = multiplicar(a, b)
        elif escolha == ':':
            resultado = dividir(a, b)

        if resultado is not None:
            print("Resultado:", resultado)
            ultimo_resultado = resultado

print(calculadora())