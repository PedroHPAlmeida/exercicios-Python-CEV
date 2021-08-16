#entrada
peso = float(input('Digite o peso (Kg): '))
altura = float(input('Digite a altura (M): '))

#processamento
imc = peso / altura ** 2

#saida
print(f'Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('Abaixo do Peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')