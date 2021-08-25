from datetime import date
#entrada & processamento
anoAtual = date.today().year
maior18 = menor18 = 0
for i in range(0, 7):
    ano =  int(input(f'Em que ano a {i + 1}ª pessoa nasceu? '))
    if anoAtual - ano < 21:
        menor18 += 1
    else:
        maior18 += 1

#saida
print(f'Ao todo tivemos {maior18} pessoas maiores de idade')
print(f'E também tivemos {menor18} pessoas menores de idade')
