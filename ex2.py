# Escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. Seu algoritmo deverá 
# mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o fim de 2024.
# Por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu programa deverá imprimir:
# Fulano de tal tem (ou terá) 34 anos

nome = input("Digite seu nome: ")
anoNascimento = int(input("Digite seu ano de nascimento: "))

idade = 2025 - anoNascimento

print(nome,"terá", idade)

