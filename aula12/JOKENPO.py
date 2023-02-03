from random import randint
from time import sleep
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0, 2)
print ('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual a sua jogada?"))
print("JO")
sleep(1.5)
print("KEN")
sleep(1.5)
print("PÔ")
sleep(0.5)
print("-=" * 11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=" * 11)

if computador == 0: #PEDRA
    if jogador == 0:#PEDRA
        print("EMPATE")

    elif jogador == 1:#PAPEL
        print("JOGADOR GANHOU! PAPEL ENROLA PEDRA")

    elif jogador == 2:#TESOURA
        print("COMPUTADOR GANHOU! PEDRA QUEBRA TESOURA")
    else:
        print("Jogada inválida!")

elif computador == 1:#PAPEL
    if jogador == 0:#PEDRA
       print("JOGADOR GANHOU! PAPEL ENROLA PEDRA")

    elif jogador == 1:#PAPEL
         print("EMPATE")

    elif jogador == 2:#TESOURA
        print("JOGADOR GANHOU! TESOURA CORTA PAPEL")
    else:
        print("Jogada inválida!")
        

elif computador == 2:#TESOURA
    if jogador == 0:#PEDRA
       print("COMPUTADOR GANHOU! PEDRA QUEBRA TESOURA")

    elif jogador == 1:#PAPEL
        print("JOGADOR GANHOU! TESOURA CORTA PAPEL")
       
    elif jogador == 2:#TESOURA
        print("EMPATE")
    else:
        print("Jogada inválida!")    