#ler uma frase #1-Quantas vezes aparela a letra 'A'.
#2-Em que posição ela aparece a primeira vez #3 Em que posição ela aparece na última vez.

frase = input('Digite sua frese: ').upper().strip()
print(len(frase))
print('Vezes que aparece a letra A na frases: {}'.format(frase.count('A')))
print('A letra "A" aparece primeiro na posição: {}'.format(frase.find('A')))
print('A letra "A" aparece por último na posição: {}'.format(frase.rfind('A')))