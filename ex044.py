#entrada
preco = float(input('Valor do produto: R$ '))

print('    FORMA DE PAGAMENTO')
print('''1 - À vista dinheiro/cheque
2 - À vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão''')
opcao = int(input('\nOpção: '))

#processamento
if opcao == 1:
    valorPagar = preco * 0.9
elif opcao == 2:
    valorPagar = preco * 0.95
elif opcao == 3:
    valorPagar = preco
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    valorPagar = preco * 1.2
    print(f'Sua compra será parcelada em {parcelas}x de R$ {valorPagar / parcelas:.2f} COM JUROS')
else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')

#saida
print(f'Total a pagar: R$ {valorPagar:.2f}')
