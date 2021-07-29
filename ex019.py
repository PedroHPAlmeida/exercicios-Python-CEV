from random import choice
alunos = []
alunos.append(input('Nome do 1º aluno(a): '))
alunos.append(input('Nome do 2º aluno(a): '))
alunos.append(input('Nome do 3º aluno(a): '))
alunos.append(input('Nome do 4º aluno(a): '))

escolhido = choice(alunos)
print(f'O aluno(a) escolhido foi: {escolhido}')
