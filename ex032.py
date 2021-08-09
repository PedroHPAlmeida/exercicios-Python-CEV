from datetime import date
#entrada
ano = int(input('Digite o ano [0 para calcular o ano atual]: '))

#processamento & saida
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto')
else: 
    print(f'{ano} NÃO é um ano bissexto')
