#entrada
n = int(input('Digite um número: '))
print('-=' * 5, f'TABUADA DO {n}', '-=' * 5)

#processamento & saida
for i in range(1, 11):
    print(f'           {n} x {i:>2} = {n * i:>2}')
print('-=' * 17)
