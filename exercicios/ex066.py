
n = s = q = 0

while True:
    n = int(input('Digite um número (999 para parar): '))

    if n == 999:
        break

    q += 1    
    s += n


print(f'A soma dos {q} valores é {s}') 
 