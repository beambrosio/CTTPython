#nome do sistema
print("Busca Sequencial")

#tupla de 1 à 20
tupla = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

#pede pro usuário digirtar qual o numero gostaria de procurar de 1 à 100
n = input("Digite um numero de 1 a 100: ")

#condicional pra ver se o numero digitado encontra-se na tupla
if n in tupla:
    print(f"O numero {n} encontrado")
else: #caso o numero não esteja na tupla, mostra pro usuário a seguinte mensagem
    print(f"O numero {n} não foi encontrado, tente outra vez! ")

