#entrada
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

#processamento
maior = r1
if r2 > maior:
    maior = r2
if r3 > maior:
    maior = r3

#saida
if ((r1 + r2 + r3) - maior) > maior:
    print('As retas acima PODEM FORMAR um triângulo')
else:
    print('As retas acima NÃO PODEM FORMAR um triângulo')
