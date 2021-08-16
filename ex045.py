from random import randint
from time import sleep
#entrada
print('''Suas opções:
0 - PEDRA
1 - PAPEL
2 - TESOURA''')
player = int(input('Qual é a sua jogada? '))

#processamento
pc = randint(0, 2)
if player < 0 or player > 2:
    print('\033[31mJogada Inválida!\033[m')
else: 
    if player == pc:
        resultado = 'EMPATE'
    elif player == 0:         #jogador jogou pedra
        if pc == 1:
            resultado = 'COMPUTADOR VENCE'
        else:
            resultado = 'JOGADOR VENCE'
    elif player == 1:         #jogador jogou papel
        if pc == 2:
            resultado = 'COMPUTADOR VENCE'
        else:
            resultado = 'JOGADOR VENCE'
    elif player == 2:         #jogador jogou tesoura
        if pc == 0:
            resultado = 'COMPUTADOR VENCE'
        else:
            resultado = 'JOGADOR VENCE'
    #saida
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(0.5)
    jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
    print('-=' * 15)
    print(f'Computador jogou {jogadas[pc]}')
    print(f'Jogador jogou {jogadas[player]}')
    print('-=' * 15)

    print(resultado)
