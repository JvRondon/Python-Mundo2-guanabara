valor = float(input("Qual o valor da casa?"))
salario = float(input("Qual seu salário atual?"))
tempo = int(input("Em quanto tempo deseja financiar a casa?"))
prestacao = valor/ (tempo * 12  )
minimo = salario * 30/100

print("Para pagar uma casa de R${} em {} anos".format(valor,tempo))
print("A prestação será de R${} por mês".format(prestacao))

if prestacao <= minimo:
    print("EMPRÉSTIMO CONCEDIDO!")
else:
    print("EMPRÉSTIMO NEGADO")