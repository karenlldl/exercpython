# Escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor de π.

num = float(input("Qual o raio do circulo?"))

area = 3.141592 * num ** 2
perimetro = 2 * 3.141592 * num

print("A área do circulo é", area, "e o perimêtro é", perimetro)