#Ler um número real e mostrar na tela a sua porção inteira
import math

num = float(input('Digite um número qualquer: '))
print('A porção inteira do número {} é {}'.format(num, math.floor(num)))
