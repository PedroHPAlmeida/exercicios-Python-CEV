#entrada
inicio = int(input('Digite o 1º termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
ultimo = inicio + 10  * razao

#processamento & saida
for i in range(inicio, ultimo, razao):
    print(f'{i} → ', end='')
print('FIM!')
