#entrada
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

#processamento & saida
cont = 1
i = primeiroTermo

while cont <= 10:
    print(f'{i} → ', end='')
    i += razao
    cont += 1
print('FIM')
