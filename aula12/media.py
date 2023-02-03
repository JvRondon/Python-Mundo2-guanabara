p1 = float(input("Nota da p1: "))
p2 = float(input("Nota da p2: "))
notaFinal = (p1+p2)/2
media = 7

if(notaFinal >= media):
    print("APROVADO!")
elif(notaFinal >= 5 and notaFinal < 7):
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")
