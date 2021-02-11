#Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
#Ler o nome dos quatro alunos e mostre a ordem sorteada

import random

a1 = input('Informe seu nome: ')
a2 = input('Informe seu nome: ')
a3 = input('Informe seu nome: ')
a4 = input('Informe seu nome: ')

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))
