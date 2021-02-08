#FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELAO SEU TIPO PRIMITIVO
#E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELE

a = input('Digite algo: ')
print(type(a))
print('É um número?',a.isnumeric()) #O (a) seria o objeto e o is. seria o metodo
print('Afanúmerico? ',a.isalnum())
print('Está em minuscula? ',a.islower())
print('Tem espaço? ',a.isspace())
print('Está em maiscula? ',a.isupper())
print('Está capitalizada?',a.istitle())
print(a.isdigit())
print(a.isdecimal())
print(a.isidentifier())
print(a.isascii())
print(a.isalpha())

