#importar biblioteca math pra automaticamente pegar o valor de pi
import math

print("Calcula área e perimetro de circulo")
#A = πr² e P=2πr. Formula de área e perimetro

#usuário entra com o valor do raio da circunferencia pra ser calculado a area e o perimetro
raio = input("Entre com o valor do raio do círculo: ")


area = (math.pi * (float(raio)) ** 2) #formula de área
perimetro = ((2 * math.pi) * float(raio)) #formula do perimetro


#mostra pro usuário a área e o perimetro dado o raio
#:.2f pra limitar duas casas depois da virgula
print(f"A area é {area:.2f}")
print(f"O perimetro é {perimetro:.2f}")

#utilizei esse site pra limitar o float
#https://pt.stackoverflow.com/questions/176243/como-limitar-números-decimais-em-python
