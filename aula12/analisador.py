somaidade=0
mediaidade=0
maioridadehomem = 0
nomevelho = ''
totmulher = 0

for i in range(1,5):
    print("-------{}° PESSOA------".format(i))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    
    somaidade += 0

    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade 
        nomevelho = nome
   
    if sexo in 'Mm' and idade> maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    
    if sexo in 'Ff' and idade<20:
        totmulher+=1

mediaidade = somaidade/4

print("A média de idade é: {}".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem,nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher))