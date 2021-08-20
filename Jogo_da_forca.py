# -*- coding: utf-8 -*-

#Hangman game(Jogo da forca)

#import
import random

forca = ['''
>>>>>>>>>>>Hangman<<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
    |
===========''','''
+---+
|   |
o   |
    |
    |
    |
    |
===========''','''
+---+
|   |
o   |
|   |
    |
    |
    |
===========''','''
 +---+
 |   |
 o   |
/|   |
     |
     |
     |
===========''','''
 +---+
 |   |
 o   |
/|\  |
     |
     |
     |
===========''','''
 +---+
 |   |
 o   |
/|\  |
/    |
     |
     |
===========''','''
 +---+
 |   |
 o   |
/|\  |
/ \  |
     |
     |
===========''']

class Hangman():

    # Método constutor
    def __init__(self, palavra):
        self.palavra = palavra
        self.errada = []
        self.certa = []

    # Método pra adivinhar a letra
    def adivinha(self,letra):
        if letra in self.palavra and letra not in self.certa:
            return self.certa.append(letra)
        elif letra not in self.palavra and letra not in self.errada:
            return self.errada.append(letra)
        else:
            return False
        return True

    # Mètodo para verificar se o jogo acabou
    def fim_jogo(self):
        return self.ganhou() or (len(self.errada)==6)

    # Método para verificar se o jogador ganhou
    def ganhou(self):
        if "_" not in self.palavra:
            return True
        return False

    # Método para não mostrar a letra no board( usar "_ ")
    def esconde_palavra(self):
        #self.esconde = self.palavra.replace(self.palavra,"_ "*len(self.palavra))
        udr = ""
        for letra in self.palavra:
            if letra not in self.certa:
                udr = "_"
            else:
                udr += letra
        return udr

    # Método para mostrar o status do game e o board(forca) na tela
    def status_jogo(self):
        print(forca[len(self.errada)])
        print(f"A palavra é: {self.esconde_palavra()}\n")
        print(f"Letras certas: {self.certa}\n")
        print(f"Letras erradas: {self.errada}\n")
        print()



# Função para buscar a palavra de forma aleatória no banco de palavras
def rand_palavra():
    with open("palavras.txt", "rt") as p:
        bank = p.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Função principal que vai iniciar o game
def main():
    #Objeto
    game = Hangman(rand_palavra())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.fim_jogo():
        game.status_jogo()
        letr = input("Digite uma letra: ")
        game.adivinha(letr)

    # Verifica o status do jogo
    game.status_jogo()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.ganhou():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()