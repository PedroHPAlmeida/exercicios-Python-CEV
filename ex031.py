#entrada
kms = int(input('Digite a distância (Km): '))

#processamento
valor = kms * 0.5
if kms > 200:
    valor = kms * 0.45

#saida
print(f'Valor a pagar R$ {valor:.2f}')
