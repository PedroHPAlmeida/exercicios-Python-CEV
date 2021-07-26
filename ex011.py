largura = float(input('Largura (metros): '))
altura = float(input('Altura (metros): '))
area = altura * largura
tinta = area / 2

print(f'Área da parede {largura:.1f}x{altura:.1f} = {area:.3f} m2')
print(f'Para pintar essa parede você precisará de {tinta:.4f}l de tinta')
