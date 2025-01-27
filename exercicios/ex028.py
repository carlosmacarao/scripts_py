from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador pensar
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

jogador = int(input("Em que numero eu pensei? ")) # Jogador tenta adivinhar

print("PROCESSANDO...")
sleep(3)

if jogador == computador:
    print("PARABÉNS! Voce conseguiu me vencer! ")
else:
    print(f"GANHEI! Eu pensei no numero {computador} e não no {jogador}")    