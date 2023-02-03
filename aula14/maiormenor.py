confirma = 'S'
soma = quant = media = 0    
while confirma in "Ss":
    n = int(input("Digíte um número: "))
    soma += n
    quant += 1


    if quant == 1:
        maior= menor = n
    else:
        if n > maior:
            maior = n
        elif n<menor:
            menor = n

    confirma = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]

media = soma/quant
print("Você digitou {} número e a média entre eles é de {}".format(quant,media))

print("O maior valor: {}. O menor valor {}.".format(maior,menor))