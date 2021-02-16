#LER UM NÚMERO E MOSTRAR OSEU DOBRO, TRILHO E RAIZ QUADRADA

n1 = float(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = pow(n1, 1/2)
print('O Dobre de \033[1;36m{}\033[m é \033[1;33m{}\033[m'.format(n1, dobro))
print('O Trilho de \033[7;30m{}\033[m é \033[1;35;44m{}\033[m'.format(n1, triplo))
print('A Raiz de \033[1;37;41m{}\033[m é \033[0;30;43m{:.3}\033[m'.format(n1, raiz))
