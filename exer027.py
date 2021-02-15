#ler nome completo - mostrar o primeiro e último nome separadamente

nome = input('DIGITE SEU NOME: ').strip().upper().split()
print('PRIMEIRO: {}'.format(nome[0]))
print('ÚLTIMO: {}'.format(nome[-1]))
