#entrada
nome = str(input('Digite seuu nome completo: ')).strip().split()

#saida
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome) - 1]))
