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
print('PROCESSANDO...')
sleep(1)

if jogador == computador:
    print('PARABÉNS! Você consegueiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
print('OBRIGADO POR JOGAR')