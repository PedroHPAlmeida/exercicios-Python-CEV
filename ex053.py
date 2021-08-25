#entrada
frase = str(input('Digite uma frase: ')).strip().upper().split()
fraseInvertida = str()

#processamento
frase = ''.join(frase)

for i in range(len(frase) - 1, -1, -1):
    fraseInvertida = fraseInvertida + frase[i]

#saida
print(f'O inverso de {frase} é {fraseInvertida}')
if frase == fraseInvertida:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
