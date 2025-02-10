
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))

    print('-' * 40)

    if n < 0:
        break

    for c in range(1, 11):
        tab = n * c
        print(f'{n} x {c} = {tab}')

    print('-' * 40)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')    
