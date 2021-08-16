#entrada
r1 = float(input('1º segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3º segmento: '))

#processamento
maior = r1
if maior < r2:    #verificando o maior segmento
    maior = r2
if maior < r3:
    maior = r3

#saida
if maior >= ((r1 + r2 + r3) - maior):
    print('Os segmentos informados NÃO PODEM formar um triângulo!')
else:
    if r1 == r2 == r3:
        print('TRIÂNGULO EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('TRIÂNGULO ISÓSCELES')
    else:
        print('TRIÂNGULO ESCALENO')
