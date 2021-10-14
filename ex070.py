print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)

totalCompra = contMaiorMil = cont = 0
maisBarato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    totalCompra += preco
    cont += 1

    if cont == 1 or preco < menorPreco:
        maisBarato = produto
        menorPreco = preco
    if preco > 1000:
        contMaiorMil += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print('-------------- FIM DO PROGRAMA --------------')
print(f'O total da compra foi R$ {totalCompra:.2f}')
print(f'Temos {contMaiorMil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {maisBarato} que custa R$ {menorPreco:.2f}')
