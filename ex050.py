#entrada
s = 0
cont = 0
for c in range(0, 6):
    n = int(input(f'Digite {c + 1}º valor: '))
    if n % 2 == 0: #processamento
        cont += 1
        s += n
#saida
print(f'Você informou {cont} números PARES e a soma foi {s}')
