#entrada
valorCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
anos = int(input('Em quantos anos deseja pagar a casa? '))

#processamento
parcelas = anos * 12
valorParcela = valorCasa / parcelas

#saida
if valorParcela <= salario * 0.3:
    print('\033[32mAprovado!\033[m')
    print(f'Você comprou uma casa no valor de R$ {valorCasa:.2f}')
    print(f'Parcelada em {parcelas} vezes de R$ {valorParcela:.2f}')
else:
    print('\033[31mNegado!\033[m')
    print('Sua renda não permite fazer esse financiamento!')
