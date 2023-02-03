total =0
num = int(input("Digite um número: "))
for c in range(1, num+1 ):
    if num%c == 0:
        print('\033[34m', end=' ')
        total +=1 
    else:
        print('\033[m',end=' ')
    print("{} ".format(c), end=' ')
print('\n\033[m0 número {} foi divisível {} vezes'.format(num,total))