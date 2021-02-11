#ler um número e mostrar o seno, cosseno e tangente desse número
from math import radians, sin, cos, tan

print("=-"*20)
print('{:=^25}'.format('SEJA BEM VINDO!!'))
print("=-"*20)
ang = float(input('Digite um angulo:'))

seno = sin(radians(ang))
tang = tan(radians(ang))
cosse = cos(radians(ang))

print(f'O ângulo de {ang}º tem o SENO de {seno:.2f}')
print(f'O ângulo de {ang}º tem o COSSENO de {cosse:.2f}')
print(f'O ângulo de {ang}º tem o TANGENTE de {tang:.2f}')
