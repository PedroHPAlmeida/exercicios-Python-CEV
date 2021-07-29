from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print(f'O valor da hipotenusa é: {hypot(co, ca):.1f}')
