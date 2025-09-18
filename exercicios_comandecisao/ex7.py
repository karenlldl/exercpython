import math

num = float(input("Digite um número: "))

if num >= 0:
    raiz = math.sqrt(num) #square root
    print(f"A raiz quadrada de {num} vale {raiz}")
else:
    print("Não é possivel extrair a raiz quadrada de número negativo")