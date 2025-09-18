numero_um = int(input("Digite o primeiro número para a divisão: "))
numero_dois = int(input("Digite o segundo número para a divisão: "))

if numero_dois == 0:
    print("Impossivel dividir por 0")
else:
    divisao = numero_um // numero_dois
    print("O resultado da sua divisão é", divisao)