# Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
resto = num_1 % num_2

if resto != 0:
    print ("O numero ", num_1," nao e divisivel pelo numero ", num_2)

else:
    print("O numero ", num_1," e divisivel pelo numero ", num_2)
