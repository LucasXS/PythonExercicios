#fazer o comput. pensar em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número
#escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('START THE GAME! - VAMOS TESTAR SUA SORTE')
print('='*60)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('='*60)

computador = randint(0, 5)
jogador = int(input('NÚMERO: '))
print('\033[1;36mPROCESSANDO...\033[m')
sleep(1)

if jogador == computador:
    print('\033[1;31mPARABÉNS!\033[m Você consegueiu me vencer')
else:
    print('\033[1;31mGANHEI!\033[m Eu pensei no número \033[1:35m{}\033[m e não no \033[1;33m{}\033[m'.format(computador, jogador))
print('OBRIGADO POR JOGAR')