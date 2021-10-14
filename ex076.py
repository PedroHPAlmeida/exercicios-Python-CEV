produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25,
         'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.30, 'Livro', 34.9)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<30} R$ {produtos[i + 1]:>6.2f}')
print('=' * 40)
