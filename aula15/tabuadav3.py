while True:
    n = int(input("Qual número deseja mostrar a tabuada? "))
    if n < 0:
        break
    print("=-="*20)
    for c in range(1,11):
        print(n," X ",c, " = ", n*c)
    print("=-="*20)
print("--"*10)
print("Programa finalizado")