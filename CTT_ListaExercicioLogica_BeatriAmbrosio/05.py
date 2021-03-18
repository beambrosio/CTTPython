print("Calcular a média do aluno! ")

#Usuário coloca o nome do aluno
nome = input("Insira o nome do(a) aluno(a): ")

#Usuário insere as quatro notas
nota1 = (input("Entre com a primeira nota: "))
nota2 = (input("Entre com a segunda nota: "))
nota3 = (input("Entre com a terceira nota: "))
nota4 = (input("Entre com a quarta nota: "))

#somando as quatro e divindo por 4
media = (int(nota1)+
        int(nota2)+
        int(nota3)+
        int(nota4))/4

#mostrando pro usuário o nome do aluno e a média que ele ficou
print(f"A média do(a) aluno(a) {nome} é {media}")