from time import sleep
#entrada
sair = False

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while not sair:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''') #menu
    opcao = int(input('>>>>> Qual é a sua opção? '))

    #processamento & saida
    if opcao < 1 or opcao > 5:
        print('\033[31mOpção inválida!\033[m')
    elif opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif opcao == 3:
        print(f'Entre {n1} e {n2} o maior é {max(n1, n2)}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        sair = True
        print('Finalizando...')
    sleep(1.5)
    print('-=' * 15)
