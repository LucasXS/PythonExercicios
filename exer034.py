#Perg. salário de func. calc. valor do aumento.
#Sal. R$1250.00 - Aumento de 10%. Sala < Aumento de 15%.

funcionario = str(input('Nome do funcionário: ')).upper().strip()
salarioAtual = float(input('Salário Atual: '))

if salarioAtual >= 1250:
    novoSalario = salarioAtual+(salarioAtual*10/100)
    print(f'O salario do(e) {funcionario} passou de {salarioAtual} para {novoSalario}')
else:
    novoSalario = salarioAtual+(salarioAtual*15/100)
    print(f'O salario do(e) {funcionario} passou de {salarioAtual} para {novoSalario}')