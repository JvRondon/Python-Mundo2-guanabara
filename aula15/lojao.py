barato= ''
maisMil = cont= menor =total = 0
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$"))
    total += preço
    resp =' '
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
    if preço > 1000:
        maisMil +=1
    if resp == "N":
        break
    if cont == 1 or preço<menor:
        preço = menor
        barato = produto
    else:
        if preço < menor:
            menor = preço
print('{:-^40}'.format("FIM DO PROGRAMA"))
print(f"Total da compra foi R${total:.2f}")
print(f"{maisMil} custam mais de mil reais")
print(f"O produto mais barato foi {menor:.2f}")