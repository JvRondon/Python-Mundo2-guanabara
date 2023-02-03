altura = float(input("Altura: "))
peso = float(input("Peso:"))
IMC = peso/(altura**2)

if IMC <= 18.5:
    print("ABAIXO DO PESO")
elif IMC > 18.5 and IMC <=25:
    print("PESO IDEAL")
elif IMC > 25 and IMC <=30:
    print("SOBREPESO")
elif IMC > 30 and IMC <=40:
    print("OBESIDADE")
else:
    print("OBESIDADE MÓRBIDA")