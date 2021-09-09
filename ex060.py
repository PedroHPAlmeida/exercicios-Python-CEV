#entrada
n = int(input('Digite um número: '))

#processamento & saida
i = n - 1
resultado = n

print(f'{n}! = {n} x ', end='')
while i > 0:
    resultado *= i
    if i > 1: 
        print(f'{i} x ', end='')
    else:
        print(f'{i} = {resultado}', end='')
    i -= 1
