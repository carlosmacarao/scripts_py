n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2

if media < 5:
    print("REPROVADO!")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO")
elif media >= 7:
    print("APROVADO!")    