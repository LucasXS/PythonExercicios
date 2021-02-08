#LER O PREÇO PRODUTO - MOSTRA SEU NOVO PREÇO COM 5% DESCONTO

nomeProduto = input('NOME DO PRODUTO: ')
precoProduto = float(input('PREÇO ATUAL R$'))

novoPrecoProduto = precoProduto - (precoProduto*5/100)
print('O {} com 5% desconto ficará R${:.2f}'.format(nomeProduto, novoPrecoProduto))
