casa = float(input("Qual o valor da casa? "))
sal = float(input("Qual o seu salário? "))
anos_pagar = int(input("Em quantos anos deseja pagar? "))

prest = casa / anos_pagar  

sal_30 = sal * 0.30

if prest <= sal_30:
    print(f"Emprestimo APROVADO! Voce irá pagar {prest} mensalmente!")
else:
    print(f"Emprestimo negado! O valor {prest} é superior a 30% do seu salário!")    