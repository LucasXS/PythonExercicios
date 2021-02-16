# ler três números e mostra qual é o maior e qual é o menor.

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
#parte 1
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'MAIOR: {n1} \nMENOR: {n3}')
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'MAIOR: {n1} \nMENOR: {n2}')
#parte 2
elif n2 > n3 and n2 > n1 and n1 > n3:
    print(f'MAIOR: {n2} \nMENOR: {n3}')
elif n2 > n3 and n2 > n1 and n3 > n1:
    print(f'MAIOR: {n2} \nMENOR: {n1}')
#parte 3
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(f'MAIOR: {n3} \nMENOR: {n1}')
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f'MAIOR: {n3} \nMENOR: {n2}')
#LADOS IGUAIS
elif n1 == n2 and n2 == n3:
    print(f'TODOS OS NÚMEROS POSSUEM O MESMO VALOR: A:{n1}, B:{n2} e C:{n3}')
#NÚMERO A É MAIOR E B E C SÃO IGUAUS
elif n1 > n2 and n1 > n3 and n2 == n3:
    print(f'MAIOR: {n1} \nIGUAIS: {n2} e {n3}')
#NÚMERO B É MAIOR E C E A SÃO IGUAUS
elif n2 > n1 and n2 > n3 and n1 == n3:
    print(f'MAIOR: {n2} \nIGUAIS: {n1} e {n3}')
#NÚMERO C É MAIOR E A E B SÃO IGUAUS
elif n3 > n1 and n3 > n2 and n1 == n2:
    print(f'MAIOR: {n3} \nIGUAIS: {n1} e {n2}')

#NÚMERO A É MENOR E B E C SÃO IGUAUS
elif n1 < n2 and n1 < n3 and n2 == n3:
    print(f'MENOR: {n1} \nIGUAIS: {n2} e {n3}')
#NÚMERO B É MENOR E A E C SÃO IGUAUS
elif n2 < n1 and n2 < n3 and n1 == n3:
    print(f'MENOR: {n2} \nIGUAIS: {n1} e {n3}')
#NÚMERO C É MENOR E A E B SÃO IGUAUS
elif n3 < n1 and n3 < n2 and n1 == n2:
    print(f'MENOR: {n3} \nIGUAIS: {n1} e {n2}')
else:
    print('ALGO DE ERRADO NÃO ESTÁ CERTO!')