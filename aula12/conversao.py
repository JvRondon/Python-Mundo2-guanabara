num = int(input("Digite um número inteiro:"))
print('''Escolha de que maneira quer que o número seja convertido:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input("Sua escolha:"))
if escolha == 1:
    print("{} convertido para binário fica {}".format(num, bin(num)[2:]))
elif escolha == 2:
      print("{} convertido para octal fica {}".format(num, oct(num)[2:]))
elif escolha == 3:
      print("{} convertido para hexadecimal fica {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida! Tente novamente")

      