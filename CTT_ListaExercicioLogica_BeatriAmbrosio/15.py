'''Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para 
o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)'''

#nome do sistema
print (" - Sistema de Feira Livre -  ")

#pede pro usuário inserir o nome
nome = input("Qual o teu nome? ")

#dá boas vindas ao usuário
print(f"Olá, {nome}, essa é nossa lista de fruta: ")

#lista com as opções de frutas pra comprar 
lista = ['1) Morango','2) Laranja', '3) Banana', '4) Acerola', '5) Uva']

#loop pra imprimir a lista pro usuário
for i in lista:
    print (i)

#pede pro usuário escolher a fruta
escolha = int(input("Qual fruta deseja comprar? "))

#incrementa a escolha do usuário pro indice começar 1 ao invés de 0
incremento = escolha - 1

#condição pra ver se o numero escolhido encontra-se na lista
if escolha > len(lista):
    print("A fruta escolhida não encontra-se na lista!")
#se tiver o numero na lista de fruta
else:    
    chosen = lista[incremento] #variavel pra armazenar a fruta escolhida
    print(f"{nome}, você escolheu comprar a fruta: {chosen}!")
