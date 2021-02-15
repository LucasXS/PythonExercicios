#ler o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('DIGITE SEU NOME: ')).upper().strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))