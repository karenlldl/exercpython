# Escrever um algoritmo que leia dois valores inteiro distintos e informe
# qual é o maior ou se houve um empate.

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

if num_1 > num_2:
    print("O maior número é", num_1)
elif num_1 == num_2:
    print("Empate")
else:
    print("Número 2 é maior")