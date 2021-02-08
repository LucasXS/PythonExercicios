#LER UM NÚMERO E MOSTRAR OSEU DOBRO, TRILHO E RAIZ QUADRADA

n1 = float(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = pow(n1, 1/2)
print('O Dobre de {} é {}'.format(n1, dobro))
print('O Trilho de {} é {}'.format(n1, triplo))
print('A Raiz de {} é {}'.format(n1, raiz))
