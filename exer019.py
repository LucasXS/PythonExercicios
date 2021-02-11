#Um professor quer sortear um dos seus quatro alunos para apagar
#o quadro. Faça um pragr. que leia o nome deles e escrendo o nome do escolhido.
#Módulo Random: Python 3

import random

n1 = input('Informe seu nome: ')
n2 = input('Informe seu nome: ')
n3 = input('Informe seu nome: ')
n4 = input('Informe seu nome: ')

print('O Aluno {} irá apagar a losa hoje'.format(random.choice([n1, n2, n3, n4])))
