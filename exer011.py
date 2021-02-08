#LER A LARGURA E ALTURA EM METROS - CALC.ÁREA E QNT TINTA NECES. P/ PINTAR - 1L = 2m**2

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
qntTintaNeces = area / 2

print('A parece possui uma área de {:.2f}m² e irá precisar de {}l tinta'.format(area,qntTintaNeces))

