#layout
print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)

#entrada
n = int(input('Quantos termos você quer mostrar? '))

#processamento & saida
anteriorDoAnterior = 0
anterior = 1
print(f'{anteriorDoAnterior} → {anterior} → ', end='')

while n - 2 != 0:
    i = anterior + anteriorDoAnterior
    print(f'{i} → ', end='')
    anteriorDoAnterior = anterior
    anterior = i
    n -= 1
print('FIM')
