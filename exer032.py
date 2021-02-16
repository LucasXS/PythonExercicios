# ler o ANO e mostar se é BISSEXTO.

#Uma das duas condições a seguir deve ser verdadeira:
#Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
#Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

from datetime import date
ano = int(input('Digite o ANO: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} É BISSEXTO')
else:
    print(f'O Ano {ano} NÃO É BISSEXTO')
