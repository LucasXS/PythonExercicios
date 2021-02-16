#ler um numero inteiro e mostrar se é PAR ou IMPAR

num = int(input('Digite um número inteiro: '))
if num % 2 == 1:
    print('O numero {} é IMPART'.format(num))
else:
    print('O numero {} é PAR'.format(num))
