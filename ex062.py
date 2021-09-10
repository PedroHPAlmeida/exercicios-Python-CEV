#entrada
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

#processamento & saida
cont = 1
i = primeiroTermo
n = 10
while cont <= n:
    print(f'{i} → ', end='')
    if cont == n:
        print('PAUSA')
        n += int(input('Quantos termos você quer mostrar a mais? '))  
    cont += 1
    i += razao
print(f'A progressão foi finalizada com {cont - 1} termos mostrados.')
