#ler o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome da cidade: ')
cidade = cidade.upper()
print('SANTO' in cidade.split()[0])
