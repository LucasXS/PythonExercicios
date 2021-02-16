# ler o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

#conferindo se é um triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Isso não é um Triângulo')
#condicionais para definir que tipo de triângulo é
elif (a == b) and (b == c) or (b == a) and (b == c):
    print('É um Triângulo Equilatero - Três lados iguais')

elif (a == b) or (b == c) or (c == a):
    print('É um Triânulo Isósceles - Dois lados quaisquer iguais')
else:
    print('É um Triângulo Escaleno - Três lados diferentes')