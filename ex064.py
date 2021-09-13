#entrada
n = s = cont = 0
while n != 999:
    s += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
    

#saida
print(f'Você digitou {cont - 1} números e a soma entre eles foi {s}.')
