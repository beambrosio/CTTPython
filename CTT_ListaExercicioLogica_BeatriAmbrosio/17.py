'''Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, nome do proprietário, data e hora da revisão. 
Depois deve guardar os dados em um dicionário e mostrar a lista de dicionários (agendamentos) na tela)'''

#nome do sistema
print("\n- Sistema de Agenda de Revisão de Carro - ")

#declaração de revisao como um dic
revisao = {}
#lista de opções do menu
lista = ["0) Sair do Sistema","1) Agenda de Revisão", "2) Mostrar os carros agendados"]

#Pede pro usuário entrar com o nome
nome = input("\nQual o teu nome? ")

print("\n - MENU - \n")
for x in lista:
    print(x)

#loop pra voltar pro menu de opções
while True:
    #pede pro usuário entrar com a opção desejada
    opc = int(input("\nQual opção gostaria?: "))
    
    #Agendar Revisão do carro
    if (opc == 1):
        #pede pro usuário digitar as informações necessarias pro agendamento
        user = str(input("\nNome do usuário que deseja fazer o agendamento: "))
        data = input("Data que deseja agendar o carro: ")
        hora = input("Qual a hora que deseja fazer o agendamento: ")
        car = input("Qual o nome do carro? ")
        ano = input("Qual o ano do carro? ")
        model = input("Qual o modelo do carro? ")

        #cria um novo dicionario temporário
        newrevisao = {}
        #armazena as informações nesse dic temporario
        newrevisao[user] = (data, hora, car, ano, model)
        #atualiza o dicionario oficial com as informações do dicionario temporario
        revisao.update(newrevisao)

        print(f"\n A revisão foi marcada:\n {newrevisao}")

    #mostra as revisões ja marcadas
    elif (opc == 2):
        print(f"\nRevisões marcadas: \n{revisao}\n")
    
    #Sair do sistema
    elif (opc == 0): 
        print("\nVocê está saindo do sistema!\n")
        break