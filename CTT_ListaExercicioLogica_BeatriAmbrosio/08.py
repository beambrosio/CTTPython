print("Calcula antecessor e sucessor dum numero inteiro positivo!")

#usuario entra com o numero que deseja saber o antecessor e sucessor
num = (input("Digite o número que deseja saber o antecessor e sucessor: "))

#checa se o numero é um inteiro positivo
if (int(num) < 0):
    #se não for inteiro positivo, retorna essa mensagem
    print("Digite um numero positivo!")
elif (int(num) > 0): #se for positivo entra nesse laço
    ante = (int(num) - 1 ) #calcula sucessor
    suc = (int(num) + 1) #calcula antecessor
    print(f"O antecessor do {num} é {ante} e o sucessor é {suc}!") #mostra na tela o numero, antecessor e sucessor
else:
    suc = (int(num) + 1) #caso seja zero o numero, ele retorna apenas o sucessor
    print(f"O antecessor desse numero é um inteiro negativo, o sucessor é {suc}!")

