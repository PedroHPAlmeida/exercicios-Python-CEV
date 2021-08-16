from datetime import date
#entrada
nasc = int(input('Ano de nascimento: '))

#processamento & saida
idade = date.today().year - nasc

print(f'O atleta tem {idade} anos')
print('Classificação: ', end='')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER') 
