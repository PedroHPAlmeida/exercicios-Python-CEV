#entrada
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

#saida
if n1 > n2:
    print(f'O primeiro valor é maior! {n1} > {n2}')
elif n2 > n1:
    print(f'O segundo valor é maior! {n2} > {n1}')
else:
    print(f'Valores iguais! {n1} = {n2}')
