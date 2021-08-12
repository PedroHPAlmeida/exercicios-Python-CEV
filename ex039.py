from datetime import date
#entrada
anoNasc = int(input('Digite o ano de nascimento: '))

#processamento
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade < 18:
    print('Você ainda não pode se alistar!')
    print(f'Faltam {18 - idade} ano(s) para o seu alistamento!')
elif idade == 18:
    print('Você deve se alistar agora!')
else:
    print('Você já devia ter se alistado!')
    print(f'Você está {idade - 18} ano(s) atrasado!')
