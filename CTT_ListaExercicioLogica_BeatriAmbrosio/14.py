print("\n~        Sistema de empréstimo de livro  ~")

nome = input("\nDigite o teu nome? ")
print(f"\nOlá {nome}, temos os seguintes livros pra emprestimo: ")

list = ['1- O Pequeno Principe','2 - O Segredo','3 - Harry Potter','4 - Game of Thrones','5 - Dom Casmurro','6 - Jogos Vorazes',
        '7 - O domo','8 - A Biblia','9 - Arte da Guerra','10 - 50 Tons de Cinza']
print(list)
value = input("\nLivro qual deseja emprestar de acordo com a numeração dele (1 - 10):  ")

ind = int(value) - 1
chosen = (list[ind])
print(f"\nVocê escolheu o livro {chosen}, {nome}! \n")

