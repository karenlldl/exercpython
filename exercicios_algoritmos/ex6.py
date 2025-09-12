# Sua tarefa é desenvolver um algoritmo que recebe um número inteiro
# de 0 a 99 e imprime o dígito das dezenas e o dígito das unidades desse número. 

num = int(input("Digite um número de 0 a 99: "))

div = num // int(10)
resto = num % int(10)

print("A dezena é", div,"e a unidade é", resto)