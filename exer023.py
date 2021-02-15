#ler um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#preciso corrigir

n1 = input('Digite um número:').strip()
print(f'Unidade:{n1[3]}\nDezena:{n1[2]:>2}\nCentena:{n1[1]}\nMilhar:{n1[0]:>2}')
