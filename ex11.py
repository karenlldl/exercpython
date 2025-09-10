# O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que recebe um RM
# e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que o aluno tenha o RM 56395, 
# seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5. 
# Dica: realize várias divisões e restos de divisões por 10.

numeroRm = int(input("Digite seu RM: "))
soma = 0
digitos = []

while numeroRm > 0:
    digito = numeroRm % 10
    soma += digito
    digitos.append(str(digito))   # guarda como string para depois juntar
    numeroRm //= 10

# inverter a ordem (porque começamos do último dígito)
digitos.reverse()

# montar a saída
expressao = " + ".join(digitos)
print(f"{soma} = {expressao}")

##fiz com ajuda do chatgpt