import random as rd  # Importando a biblioteca random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    total_de_tentativas = 0
    numero_secreto = rd.randrange(1, 101)  # Função para randomizar números entre 1 e 100
    pontos = 1000

    print("Qual é o nível de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int(input("Defina o nível de dificuldade: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite o seu número entre 1 e 100: "))
        print("Você digitou", chute)

        if chute < 1 or chute > 100:
            print("\n Você deve chutar um número entre 1 e 100.")
            continue  # Volta ao for anterior

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou!")
            print("A sua pontuação foi de {}!".format(pontos))
            break
        elif maior:
            print("Você errou! O seu chute foi maior que o número secreto.")
        else:
            print("Você errou! O seu chute foi menor que o número secreto.")
        pontos = pontos - abs(chute - numero_secreto)

    print("Fim do jogo!")
    print(numero_secreto)


if __name__ == "__main__":
    jogar()
