#CONVERSOR DE TEMPERATURA

celcius = float(input('Informe a temperatura em ºC: '))
fahrenheit = (celcius * 9/5) + 32
print('{}ºC é equivalente a {}ºF (Fahrenheit)'.format(celcius,fahrenheit))
fahrenheit = float(input('Informe a temperatura em ºF: '))
celcius = (fahrenheit - 32) * 5/9
print('{}ºF é equivalente a {}ºC (Celcius)'.format(fahrenheit, celcius))

