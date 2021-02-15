#ler o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip().upper()
print(cidade[:5] == 'SANTO') #correção
print('SANTO' in cidade.split()[0]) #como eu fiz
