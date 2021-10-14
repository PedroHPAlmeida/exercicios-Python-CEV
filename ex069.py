cont18 = contHomem = contMulher20 = 0
while True:
    print("-" * 30)
    print(f"{'CADATRE UMA PESSOA':^30}")
    print("-" * 30)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F' and idade < 20:
        contMulher20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {contHomem} homens cadastrados')
print(f'E temos {contMulher20} mulheres com menos de 20 anos')
