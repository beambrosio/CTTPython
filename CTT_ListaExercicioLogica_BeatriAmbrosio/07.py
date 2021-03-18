print("Sistema de loteria")

#numero aleatório da loteria definida por mim
lot = ["1","12","26","34","50","87","99"]

#insira o nome do apostador
nome = input("Nome do apostador: ")
#insira o numero que vai apostar
guess = input("Entre com um numero e adivinhe se voce ganhou a loteria!: ")

#condição pra checar se o numero inserido tem na loteria
if guess in lot:
    #caso positivo, entra nesse if
    print(f"{nome}, você digitou {guess} e adivinhou o numero da loteria e o professor Jeff te deve uma coxinha!" )
else:
    #se nao, retorna essa mensagem
    print(f"Epa {nome}, não foi dessa vez, mas não desista!")

