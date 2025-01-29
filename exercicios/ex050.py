for c in range(1, 6+1):
    n = int(input("Digite um número inteiro: "))

s = 0
if n % 2 == 0:
    s += n
    print(f"A soma dos pares é: {s}")
else:
    print("Não considerado!")    

