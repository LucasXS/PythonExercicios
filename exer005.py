#LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

n = float(input('Digite um número: '))
print('A partir do número \033[1;31m{}\033[m sabemos que seu: \nSucessor é \033[1;33m{}\033[m \nAntecessor é \033[1;32m{}\033[m'.format(n, n+1, n-1))
