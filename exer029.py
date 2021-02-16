# ler a veloc. um carro. Se passar de 80Km/h, mostrre uma msg que ele foi multado. A multa R$7.00 p/Km acima do limite

velocidade = float(input('Velocidade final: '))
if velocidade > 80:
    print('Voce estava acima da velocidade permitida de 80Km. Será multado por isso.')
    multa = (velocidade - 80) * 7
    print('Sua multa total é de R${:.2f}, com vencimento para daqui 7 dias úteis!'.format(multa))
print('Tenha um bom dia! Diriga com segurança!')