from math import sin, cos, tan, radians
angulo = int(input('Digite um ângulo: '))

seno = sin(radians(angulo))
cossen = cos(radians(angulo))
tang = tan(radians(angulo))

print(f'Seno de {angulo}° = {seno:.2f}')
print(f'Cosseno de {angulo}° = {cossen:.2f}')
print(f'Tangente de {angulo}° = {tang:.2f}')
