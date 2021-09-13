#entrada
resp = 'S'
media = cont = maior = menor = 0

while resp == 'S':
    n = int(input('Digite um número: '))
    
    #processamento
    media += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media /= cont

#saida
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
