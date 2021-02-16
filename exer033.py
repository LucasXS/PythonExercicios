# ler três números e mostra qual é o maior e qual é o menor.

a = float(input('Digite o 1º número: '))
b = float(input('Digite o 2º número: '))
c = float(input('Digite o 3º número: '))

#parte 1
if a > b and a > c and b > c:
    print(f'MAIOR: {a} \nMENOR: {c}')
elif a > b and a > c and c > b:
    print(f'MAIOR: {a} \nMENOR: {b}')
#parte 2
elif b > c and b > a and a > c:
    print(f'MAIOR: {b} \nMENOR: {c}')
elif b > c and b > a and c > a:
    print(f'MAIOR: {b} \nMENOR: {a}')
#parte 3
elif c > a and c > b and b > a:
    print(f'MAIOR: {c} \nMENOR: {a}')
elif c > a and c > b and a > b:
    print(f'MAIOR: {c} \nMENOR: {b}')

#LADOS IGUAIS
elif a == b and b == c:
    print(f'TODOS OS NÚMEROS POSSUEM O MESMO VALOR: A:{a}, B:{b} e C:{c}')
#NÚMERO A É MAIOR E B E C SÃO IGUAUS
elif a > b and a > c and b == c:
    print(f'MAIOR: {a} \nIGUAIS: {b} e {c}')
#NÚMERO B É MAIOR E C E A SÃO IGUAUS
elif b > a and b > c and a == c:
    print(f'MAIOR: {b} \nIGUAIS: {a} e {c}')
#NÚMERO C É MAIOR E A E B SÃO IGUAUS
elif c > a and c > b and a == b:
    print(f'MAIOR: {c} \nIGUAIS: {a} e {b}')

#NÚMERO A É MENOR E B E C SÃO IGUAUS
elif a < b and a < c and b == c:
    print(f'MENOR: {a} \nIGUAIS: {b} e {c}')
#NÚMERO B É MENOR E A E C SÃO IGUAUS
elif b < a and b < c and a == c:
    print(f'MENOR: {b} \nIGUAIS: {a} e {c}')
#NÚMERO C É MENOR E A E B SÃO IGUAUS
elif c < a and c < b and a == b:
    print(f'MENOR: {c} \nIGUAIS: {a} e {b}')
else:
    print('ALGO DE ERRADO NÃO ESTÁ CERTO!')