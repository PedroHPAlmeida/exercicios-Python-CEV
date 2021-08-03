#entrada
cidade = str(input('Digite o nome da sua cidade: ')).strip()

#saída
print(f'Sua cidade começa com "Santo": {"santo" in cidade.lower().split()[0]}')
