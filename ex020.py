from random import shuffle
#entrada
a1 = input('Nome 1º aluno(a): ')
a2 = input('Nome 2º aluno(a): ')
a3 = input('Nome 3º aluno(a): ')
a4 = input('Nome 4º aluno(a): ')

#processamento
lista = [a1, a2, a3, a4]
shuffle(lista)

#saída
print(f'Ordem de apresentação: {lista}')
