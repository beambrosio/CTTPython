'''Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, Imprimir os dados do dicionário, 
ser capaz de inserir e excluir um contato)'''

#nome do sistema
print(" - Agenda de Contatos - ")

#pede pro usuário falar qual o nome
nome = input("\nQual teu nome? ")
#inicializa a variavel agenda como um dicionario
agenda = {}

#lista de opções de escolha
lista = ["0) Sair", "1) Inserir contato", "2) Imprimir os dados", "3) Excluir contato"]

print("\n")
#mostra pro usuário os itens da lista
for y in lista:
    
    print(y)

#loop pra sempre pedir opção do contato
while True:
    x = int(input("\nQual tua opção: ")) #pede pro user escolher a opção e converte de str pra int

    #Inserir contato
    if (x == 1):

        #pede as infomações do usuário
        contato = str(input("Qual o nome do contato? "))
        tel = str(input("Qual o telefone? "))
        endereco = str(input("Qual o endereço? "))

        #inicializa variavel como dicionario pra poder atualizar
        newagenda = {}
        #armazena no novo dicionario contato como key e tel e endereço com value
        newagenda[contato] = (tel, endereco)
        #da append na lista de input pra lista oficial do sistema
        agenda.update(newagenda)

    #Imprimir o contato
    if (x == 2):

        print("\nContatos salvos:B")
        print(f"{agenda}\n")

    #Excluir o contato
    if (x == 3):

        #pede pro usuario falar qual deseja deletar        
        deletar = str(input(f"Qual contato deseja excluir? "))
        agenda.keys()

        #pesquisa se existe na agenda
        if deletar in agenda:
            agenda.pop(deletar) #excluir da lista tirando o contato desejado

        print(f"\nLista atualizada: \n{agenda}\n") #mostra pro usuário a nova lista

    #Sair do sistema
    if x == 0:
        print("\nVoce está saindo do programa!\n")
        break
        


