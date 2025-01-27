nome = str(input("Qual é o seu nome: ")) 

if nome == "Carlos":
    print("Que nome bonito!")
elif nome == "Zidane" or nome == "Manuel" or nome == "Imaldo":
    print("Este nome me lembra um dos meus amigos!")   
elif nome in "Solange Silvia Helena Marcia":
    print("Uma das mulheres da minha vida!")
else:
    print("Seu nome é bem normal!")    
