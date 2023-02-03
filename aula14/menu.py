n1 = int(input("n1: "))
n2 = int(input("n2: "))
opção = 0

soma=n1+n2
multiplicação = n1*n2

while opção !=5:
    
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair''')
    opção = int(input("-------Qual a sua opção?------- "))
    if opção == 1:
        print("A soma entre {} e {} é {}".format(n1,n2,soma))
    elif opção == 2:
        print("A multiplicação entre {} e {} é {}".format(n1,n2,multiplicação))
    elif opção == 3:
        if(n1>n2):
            print("{} é maior".format(n1))
        else:
            print("{} é maior".format(n2))
    elif opção == 4:
        print("Informe novamente os valores!")
        n1 = int(input("n1: "))
        n2 = int(input("n2: "))
    elif opção == 5:
        print("Já deu!")
    else:
        print("Opção inválida! Selecione uma que corresponda...")
    print('=-='*10)
