print('{:=^40}'.format(" LOJÃO DO JÃO "))
preço = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO 
[ 1 ] à vista DINHEIRO/CHEQUE
[ 2 ] à vista no CARTÃO
[ 3 ] 2x no CARTÃO
[ 4 ] 3x OU MAIS ou CARTÃO
''')
opção = int(input("Qual a opção desejada? "))

if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço* 5/100)
elif opção == 3:
    total = preço 
    parcela = preço/2
    print("Sua compra parcelada em 2x de {:.2f} SEM JUROS.".format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input("Quantas parcelas?"))
    parcela = total/totparc
    print("Sua compra será parcelada em {}x de {:.2f} COM JUROS".format(totparc,parcela))
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço,total))
