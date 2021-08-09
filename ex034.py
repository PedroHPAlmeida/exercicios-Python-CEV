#entrada
salario = float(input('Digite o salário do funcionário: R$ '))

#processamento
salarioComAumento = salario * 1.15 if salario <= 1250 else salario * 1.1

#saida
print(f'Novo salário do funcionário: R$ {salarioComAumento:.2f}')
