#entrada
velocidade = int(input('Digite a velocidade do carro: '))

#processamento & saida
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado! Limite permitido é de 80Km/h')
    print(f'Valor a pagar: R$ {multa:.2f}')
else:
    print('Boa viagem! Dirija com segurança!')
