import random

def obter_escolha_computador():
    lista_palavras = ["pedra", "papel", "tesoura"]
    return random.choice(lista_palavras)

def obter_escolha_usuario():
    escolha = input("Escolha (pedra, papel, tesoura): ")
    while escolha not in ["pedra", "papel", "tesoura"]:
        print("Opção inválida!")
        escolha = input("Escolha pedra, papel, tesoura: ")
    return escolha

def determinar_vencedor(usuario, computador):
    print(f"Jogador 1 escolheu {usuario}, Jogador 2 escolheu {computador}.")
    if usuario == computador:
        return "Empate!"
    elif (usuario == "pedra" and computador == "tesoura"): 
        return "Jogador 1 venceu!"
    elif (usuario == "papel" and computador == "pedra"):
        return "Jogador 1 venceu!"
    elif (usuario == "tesoura" and computador == "papel"):
        return "Jogador 1 venceu!"
    else:
        return "Jogador 2 venceu!"

def jogo():
    while True:
        jogador1 = obter_escolha_usuario()
        jogador2 = obter_escolha_computador()
        print(determinar_vencedor(jogador1, jogador2))
        
        continuar = input("Jogar novamente? (sim/nao): ")
        if continuar != 'sim':
            break
    return("Obrigado por jogar!")

print(jogo())



