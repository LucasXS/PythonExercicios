#SOMAR DOIS NUMEROS E MOSTRAR NA TELA, USAR O .FORMAT.

n1 = int (input('Digite um valor: '))
n2 = int (input('Digite um valor: '))
s = n1 + n2
#print('A soma entre',n1, 'e', n2,' vale', s) sem o .format
print('A Soma entre \033[4;33m{}\033[m e \033[4;35m{}\033[m vale \033[1;31;46m{}\033[m'.format(n1, n2, s)) #com o .format
