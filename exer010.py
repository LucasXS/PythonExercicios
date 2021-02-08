#LER QUANTO DINHEIRO UMA PESSOA TEM E CONVERTER P/ OUTRAS MOEDAS - 07/02/2021

emReal = float(input('Quanta grana você tem? R$'))
emDolar = emReal / 5.37
emEuro = emReal / 6.47
emIene = emReal /0.051
print('R${} reais dá exatamente \n${:.2f} dolares \n€{:.2f} Euros \n¥{:.2f} Ienes'.format(emReal, emDolar, emEuro, emIene))
