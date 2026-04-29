def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        print('INDEFINIDO')
    return a / b

a = float(input("Digite o primeiro número: "))

def calculadora():
    print("Selecione a operação:")
    print("+. Somar")
    print("-. Subtrair")
    print(":. Multiplicar")
    print("x. Dividir")

    escolha = input("Digite sua escolha (+/-/x/:): ")

    b = float(input("Digite o segundo número: "))

    if escolha in ('+', '-', ':', 'x'):

        if escolha == '+':
            print ("Resultado:", somar(a, b))
        elif escolha == '-':
            print ("Resultado:", subtrair(a, b))
        elif escolha == 'x':
            print ("Resultado:", multiplicar(a, b))
        elif escolha == ':':
            print ("Resultado:", dividir(a, b))
    else:
        return("Escolha inválida")
   
print(calculadora())
    