#entrada
n = int(input('Digite um número: '))
print('''1- para binário\n2- para octal\n3- para hexadecimal''')
opcao = int(input('Sua opcao: '))

#saida
if opcao == 1:
    print(f'{n} em binário = {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} em octal = {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} em hexadecimal = {hex(n)[2:]}')
else:
    print('\033[31mOpção Inválida!\033[m')
