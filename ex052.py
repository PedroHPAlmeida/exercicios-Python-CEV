#entrada
n = int(input('Digite um número: '))

#processamento
divisivel = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(f'\033[33m{i}\033[m', end=' ')
        divisivel += 1 
    else: 
        print(f'\033[31m{i}\033[m', end=' ')

#saida
print(f'\nO número {n} foi divisível {divisivel} vez(es)')
if divisivel == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
