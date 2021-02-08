#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
#carro custa R$60 por dia e R$0,15 por Km rodado.

nomeCliente = input('Informe o nome do cliente: ')
nomeCarro = input('Nome do carro augado:')
diasAlugados = int(input('Quantos dias alugados? '))
kmRodados = float(input('Quantos Km rodados? '))

custoTotal = ((60 * diasAlugados) + (kmRodados * 0.15))

print('O cliente {} por ter alugado o carro {} por {} dias pagará '
      'um valor de R${}'.format(nomeCliente,nomeCarro, diasAlugados, custoTotal))
