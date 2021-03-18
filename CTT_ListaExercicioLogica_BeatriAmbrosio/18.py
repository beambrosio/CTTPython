'''Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), pedir o nome do usuário e fazer com o que o usuário 
selecione um objeto e imprimir a compra na tela)'''

#nome do sistema
print("\n- Sistema de Compras -\n")

#declarações
carrinho = []
objetos = { 'cadeira': ('100,00', 'Madeira'), 
            'caixa de lápis':('36,00','12 Cores'), 
            'Tesoura': ('5,00','Vermelha'),    
            'Régua':('12,00','Transparente') }

opcoes = ["0) Sair do Sistema","1) Exibir lista de objetos","2) Colocar objetos no carrinho", "3) Mostrar carrinho"]

#pede pro usuario entrar com o nome
nome = input("Qual o teu nome? " )

#loop para imprimir a lista de opções pro usuário
print("\n")
for x in opcoes:
    print(x)

#laço pra voltar no menu de escolha
while True:
    #pede pro usuário entrar com a opção desejada do menu
    opc = int(input("\nQual opção deseja selecionar: "))

    #Exibir lista de objetos
    if (opc == 1):
        print("\n - Lista de Objetos - ")
        for x in objetos.items():
            print (x)

    #Colocar objetos no carrinho
    if (opc == 2):
        compra = str(input(f"Qual item deseja comprar? Entre com o nome do objeto: "))
        
        #verifica se o item desejado encontra-se na lista
        for item in objetos.keys(): 
            if (compra == item):
                
                #coloca no carrinho o item pra comprar
                carrinho.append(item + str(objetos.get(compra)))

    #Mostrar a lista de compra
    if (opc == 3):

        print(f"\n{carrinho}")
    
    #Sair do sistema
    if (opc == 0):
        print("\nVoce está saindo do programa!\n")
        break
