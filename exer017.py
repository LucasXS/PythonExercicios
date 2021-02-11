#ler o comprim cateto oposto e cateto adjacente (triag. retang). Cal. e mostre o compr. da hipotenusa.

print("="*25)
print('{:=^25}'.format('SEJA BEM VINDO!!'))
print("="*25)
import math
print("Insira o cateto oposto e adjacente para calcular a hipotenusa!")

catOposto = float(input('Digite o valor do cateto oposto: '))
catAdjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(catOposto, catAdjacente)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
print('ESPERO TER AJUDADO!')
