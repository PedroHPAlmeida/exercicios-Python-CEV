#entrada
frase = str(input('Digite uma frase: ')).upper().strip().split()
frase = ''.join(frase) #para desconsiderar os espaços entre as palavras

#saida
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela 1ª vez na posição: {}'.format(frase.find('A') + 1))
print('A letra "A" aparece pela última vez na posição: {}'.format(frase.rfind('A') + 1))
