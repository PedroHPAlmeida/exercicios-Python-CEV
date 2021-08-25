#entrada & processamento
for i in range(0, 5):
    peso = float(input(f'Peso da 1ª pessoa: '))
    if i == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

#saida
print(f'O maior peso lido foi de {maior:.2f}Kg')
print(f'O menor peso lido foi de {menor:.2f}Kg')
