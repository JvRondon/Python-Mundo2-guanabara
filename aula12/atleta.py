from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print("O atleta tem {} anos".format(idade))
if(idade <=9):
    print("Classificação: MIRIM")
elif(idade > 9 and idade <=14):
    print("Classificação: INFANTIL")
elif(idade > 15 and idade <=19):
    print("Classificação: JUNIOR")
elif(idade > 20 and idade <=25):
    print("Classificação: SÊNIOR")
elif(idade > 26):
    print("Classificação: MASTER")