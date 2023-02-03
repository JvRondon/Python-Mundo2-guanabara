sexo = str(input("informe seu sexo: ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados inválidos, verifique e tente novamente: "))
print("Sexo {} registrado com sucesso").format(sexo)
    