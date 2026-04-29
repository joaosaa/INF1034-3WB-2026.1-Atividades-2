import random

def usuario_adivinha():
    numero = random.randint(1, 1023)
    tentativas = 0

    print("Tente adivinhar o número (entre 1 e 1023):")

    while True:
        palpite = int(input("Palpite: "))
        tentativas += 1

        if palpite == numero:
            print(0)
            print(f"Acertou em {tentativas} tentativas!")
            break

        if palpite > numero:
            print(-1)
        else:
            print(1)

def computador_adivinha():
    print("Pense em um número entre 1 e 1023...")

    minimo = 1
    maximo = 1023
    tentativas = 0

    while True:
        palpite = random.randint(minimo, maximo)
        tentativas += 1

        print(f"Eu acho que é: {palpite}")
        resposta = int(input("Digite -1 se seu número for menor, 1 se for maior, 0 se acertei: "))

        if resposta == -1:
            maximo = palpite - 1
        elif resposta == 1:
            minimo = palpite + 1
        elif resposta == 0:
            print(f"Acertei em {tentativas} tentativas!")
            break
        else:
            print("Resposta inválida.")


def jogar():
    print('ESSE É O JOGO DA ADIVINHAÇÃO')
    print("Quem vai tentar adivinhar?")
    print("1 - Usuário")
    print("2 - Computador")

    escolha = int(input("Escolha (1 ou 2): "))

    if escolha == 1:
        usuario_adivinha()
    elif escolha == 2:
        computador_adivinha()
    else:
        print("Opção inválida.")

print(jogar())
