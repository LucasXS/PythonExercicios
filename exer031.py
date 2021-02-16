#Perg. a distância de uma viagem em Km. Calc. preço da passagem, cobrando R$0.50 p/Km para viagens até 200Km e R$0.45
# p/ mais longas.

cidadeAtual = str(input('Digite a cidade de partida: ')).strip().upper()
cidade = str(input('Digite a cidade destino: ')).upper().strip()
distancia = float(input('Digite a distância total do trajeto: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('A passagem de {} para {} custará R${:.2f}'.format(cidadeAtual, cidade, valor))
else:
    valor = distancia * 0.45
    print('A passagem de {} para {} custará R${:.2f}'.format(cidadeAtual, cidade, valor))

#valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
#print('A passagem de {} para {} custará R${:.2f}'.format(cidadeAtual, cidade, valor))