#entrada
n = int(input('Digite um número [0 - 9999]: '))

#processamento
m = n // 1000
c = n % 1000 // 100
d = n % 1000 % 100 // 10
u = n % 1000 % 100 % 10 

#saída
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
