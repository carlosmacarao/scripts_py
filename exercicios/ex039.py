ano_nasc = int(input("Digite o seu ano de nascimento: "))

idade = 2025 - ano_nasc

print(f"Voce tem {idade} anos.")
if idade < 18:
    print("Voce ainda vai se alistar ao serviço militar!")
elif idade == 18:
    print("Esta na hora de se alistar!")
else:
    print("Já passou o tempo do alistamento!")        