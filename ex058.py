from random import randint 
#entrada
numPc = randint(0, 10)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
numJogador = int(input('Qual é seu palpite? '))

tentativas = 1

while numJogador != numPc:
    if numJogador < numPc:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez')

    numJogador = int(input('Qual é seu palpite? '))
    tentativas += 1

#saida
print(f'Acertou com {tentativas} tentativas. Parabéns!')
