# Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses dois números, 
# a multiplicação, a divisão inteira e o resto da divisão inteira.

numUm = int(input("Digite o primeiro número: "))
numDois = int(input("Digite o segundo número: "))

soma = numUm + numDois
multiplicacao = numUm * numDois
div = numUm // numDois
resto = numUm % numDois

print("A soma é", soma)
print("A multiplicacao é", multiplicacao)
print("A divisão é", div)
print("O resto é", resto)