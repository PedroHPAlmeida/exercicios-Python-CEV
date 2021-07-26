dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preco = dias * 60 + 0.15 * km

print(f'Total a pagar: R$ {preco:.2f}')
