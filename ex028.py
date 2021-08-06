from random import randint
from emoji import emojize
from time import sleep
#entrada
pc = randint(0, 5)
print('Pensei em um número entre 0 e 5, tente adivinhar...')
player = int(input('Digite: '))

#processamento & saída
print('Processando...')
sleep(1.5)
print(f'PC = {pc}\nVocê = {player}')
if player == pc:
    print('Parabéns, você acertou! {}'.format(emojize(':sunglasses:', use_aliases=True)))
else:
    print('Que pena! Você perdeu! {}'.format(emojize(':sob:', use_aliases=True)))
