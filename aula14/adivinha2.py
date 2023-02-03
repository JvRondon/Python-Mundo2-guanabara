from random import randint
computador = randint(1,10)
print("Sou seu computador.. Pensei em um número de 0 a 10")
print("Adivinhe!")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual o seu palpite?"))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if (jogador > computador):
            print("Menor...")
        elif(jogador < computador):
            print("Maior...")
print("Acertou com {} palpites.".format(palpite))