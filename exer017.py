#ler o comprim cateto oposto e cateto adjacente (triag. retang). Cal. e mostre o compr. da hipotenusa.

print("="*25)
print('{:=^25}'.format('SEJA BEM VINDO!!'))
print("="*25)
from math import sqrt
print("Insira o cateto oposto e adjacente para calcular a hipotenusa!")

catOposto = float(input('Digite o valor do cateto oposto: '))
catAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (catOposto*catOposto)+(catAdjacente*catAdjacente)
res = sqrt(hipotenusa)
print('O valor da hipotenusa é {:.2}'.format(res))
print('ESPERO TER AJUDADO!')
