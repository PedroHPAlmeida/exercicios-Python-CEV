#entrada & processamento
media = idadeHomemMaisVelho = mulherMenos20Anos = 0
for i in range(0, 4):
    print(f'----- {i + 1}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))[0].upper()

    media += idade #calculando a media de idade do grupo
    if sexo == 'M':
        if idade > idadeHomemMaisVelho: #verificando o homem mais velho
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome
    else:
        if idade < 20: #verificando mulheres com menos de 20 anos
            mulherMenos20Anos += 1
media /= (i + 1)

#saida
print(f'A média de idade do grupo é de {media:.1f} anos')
print(f'O homem mais velho tem {idadeHomemMaisVelho} anos e se chama {nomeHomemMaisVelho}')
print(f'Ao todo são {mulherMenos20Anos} mulher(es) com menos de 20 anos')
