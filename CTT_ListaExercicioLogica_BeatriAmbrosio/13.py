print("\n~       Guia de viagem       ~")

#usuário entra com o nome
print("\nOlá, vamos viajar?")
nome = input("\nPrimeiro me diga o seu nome: ")

#mostra lista de opções de viagem
print(f"\n{nome}, temos essas opções de viagem pra você: | 1) Rio de Janeiro | 2) Londres | 3) Nova York | 4) Japão")

#usuário entra com a opção que gostaria
choice = input("Me fale pra onde deseja ir: ")


#ifs e mensagens personalizadas pra cada local
if (choice == '1'):
    print(f"\nVamos então visitar o Cristo Redentor, {nome}!\n")
elif (choice == '2'):
    print(f"\nHey, {nome}, let's go visit the Big Bang, Sherlock!\n")
elif (choice == '3'):
    print(f"\nHey,{nome}, wanna hang out in Central Park?\n")
elif (choice == '4'):
    print(f"\nKon'nichiwa, {nome}\n")