n = int(input("Digite um número para ver a tabuada: "))

for c in range(1, n+1):
    tab = n * c
    print(f"{n} x {c} = {tab}")