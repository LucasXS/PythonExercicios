#ler o nome completo e mostrar. 1-nome com letras MAISCULAS 2-Qnts letras ao total 3-Qnts letras tem 1 nome

nome = str(input('Informe o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maisculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' '))) #remv os espaços branco entre as palv.
