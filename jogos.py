import forca
import adivinhacao


def escolher_jogos():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca  (2) Adivinhação")

    jogo = int(input("Escolha o seu jogo: "))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()


if __name__ == "__main__":  # Não executar a função importada
    escolher_jogos()
