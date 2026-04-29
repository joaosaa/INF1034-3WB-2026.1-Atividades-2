import random

print("Esse é o jogo da forca!")
print("O TEMA É: FRUTAS")

palavras = ["banana", "morango", "uva", "laranja", "manga", "abacaxi"]

def escolher_palavra():
    return random.choice(palavras)

def jogar():

    palavra = escolher_palavra()

    letras_usuario = []
    chances = 6
    ganhou = False

    while True:

        for letra in palavra:
            if letra in letras_usuario:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        print(f"{chances} chances")

        tentativa = input("Digite uma letra ou a palavra: ")

        if len(tentativa) > 1:
            if tentativa == palavra:
                ganhou = True
                break
            else:
                chances -= 1
        else:
            if tentativa not in letras_usuario:
                letras_usuario.append(tentativa)

            if tentativa not in palavra:
                chances -= 1

        ganhou = True
        for letra in palavra:
            if letra not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f'Parabéns, você ganhou! A palavra era: {palavra}')
    else:
        print(f'Você perdeu! A palavra era: {palavra}')


while True:
    jogar()
    if input('Quer jogar novamente? (sim/nao): ') != "sim":
        break