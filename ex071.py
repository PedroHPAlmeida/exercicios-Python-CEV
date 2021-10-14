print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)

valor = float(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
totalCed = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cédulas de R$ {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCed = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV!')
