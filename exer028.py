#fazer o comput. pensar em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número
#escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
print('{:=^15}'.format('STAR GAME! - VAMOS TESTAR SUA SORTE'))
print('{:=^15}'.format('DIGITE UM NÚMERO ENTRE 0 E 5'))
numero = random.randint(0, 5)
num = int(input('NÚMERO: '))
if num == numero:
    print('Você acertou! O número pensado pelo computador era {}'.format(numero))
else:
    print('Você perdeu! O número pensado pelo computador era {}'.format(numero))
print('{:=^15}'.format('OBRIGADO POR JOGAR'))
