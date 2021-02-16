#FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELAO SEU TIPO PRIMITIVO
#E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELE

a = input('Digite algo: ')
print(type(a))
print('\033[1;36mÉ um número?\033[m', a.isnumeric()) #O (a) seria o objeto e o is. seria o metodo
print('\033[1;36mAfanúmerico?\033[m', a.isalnum())
print('\033[1;36mEstá em minuscula?\033[m', a.islower())
print('\033[1;36mTem espaço?\033[m', a.isspace())
print('\033[1;36mEstá em maiscula?\033[m', a.isupper())
print('\033[1;36mEstá capitalizada?\033[m', a.istitle())
print(a.isdigit())
print(a.isdecimal())
print(a.isidentifier())
print(a.isascii())
print(a.isalpha())

