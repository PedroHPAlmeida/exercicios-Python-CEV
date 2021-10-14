while True: #entrada
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 30)

    if n < 0: #condicao de parada
        break
    #saida
    for i in range(1, 11):
        print(f"{n} x {i:>2} = {n * i:>2}")
    print("-" * 30)
print("PROGRAMA TABUADA ENCERRADO")
