times = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Bragantino', 'Palmeiras', 'Corinthians', 'Internacional', 'Athletico-PR', 'Fluminense', 'Atlético-GO')
print('=-=' * 10)
print(f'Lista dos times do Brasileirão: {times}')
print('=-=' * 10)
print(f'Os 5 primeiros são: {times[:5]}')
print('=-=' * 10)
print(f'Os 4 últimos são: {times[-4:]}')
print('=-=' * 10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-=' * 10)
print(f'O Palmeiras está na {times.index("Palmeiras") + 1}ª posição')