#entrada
frase = str(input('Digite uma frase: ')).strip().upper().split()
fraseInvertida = str()

#processamento
frase = ''.join(frase)

#fraseInvertida = frase[::-1] - Forma simples de inverter uma frase usando tecnicas de fatiamento 

for i in range(len(frase) - 1, -1, -1):
    fraseInvertida = fraseInvertida + frase[i]

#saida
print(f'O inverso de {frase} é {fraseInvertida}')
if frase == fraseInvertida:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
