#LER O SALÁRIO DE UMA FUNCIONÁRIA E MOSTRAR SEU NOVO SALÁRIO COM 15% DE AUMENTO

nomeFuncionario = input('NOME FUNCIONARIO: ')
salarioAtualFunc = float(input('SALÁRIO ATUAL R$'))

novoSalario = salarioAtualFunc + (salarioAtualFunc * 15/100)
print('O Funcionário {} deixará de receber {:.2f} e passará a receber {:.2f}'.format(nomeFuncionario, salarioAtualFunc, novoSalario))
