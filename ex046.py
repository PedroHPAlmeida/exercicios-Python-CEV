from time import sleep
from emoji import emojize
#saida
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize('Feliz Ano Novo :boom::boom::boom:', use_aliases=True))
    