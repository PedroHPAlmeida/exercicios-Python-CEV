#entrada
nome = str(input('Digite seu nome completo: ')).strip()

#saída
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print('Quantidade de letras (sem espaços): {}'.format(len(nome) - nome.count(' ')))
print(f'Primeiro nome: {nome.split()[0]} -> {len(nome.split()[0])} letras')
