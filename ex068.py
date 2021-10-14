from random import randint

print("=-=" * 10)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-=" * 10)

cont = 0
while True:
    n = int(input("Digite um valor: "))
    pc = randint(0, 10)
    soma = n + pc

    parOuImpar = ' '
    while parOuImpar not in 'PI':
        parOuImpar = str(input("Par ou Ímpar? [P/I] ")).strip()[0].upper()

    print("-" * 30)
    print(f"Você jogou {n} e o computador {pc}. Total de {soma} DEU {'PAR' if soma % 2 == 0 else 'ÍMPAR'}")
    print("-" * 30)

    if soma % 2 == 0 and parOuImpar == "P" or soma % 2 == 1 and parOuImpar == "I":
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        print("=-=" * 10)
        cont += 1
    else:
        print("Você PERDEU!")
        print("=-=" * 10)
        break

print(f"GAME OVER! Você venceu {cont} vez(es)")
