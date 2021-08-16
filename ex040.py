#entrada
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

#processamento
media = (n1 + n2) / 2

#saida
print(f'Média: {media:.1f}')
if media < 5:
    print('\033[31mREPROVADO\033[m')
elif media < 7:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO\033[m')
