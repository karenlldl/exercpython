valorAvista = float(input("Digite o valor do IPTU a vista: "))
parcelado = float(input("Digite o valor de cada parcela: "))

diferenca = parcelado * 10

valorDesconto = diferenca / valorAvista
valorDesconto = 1 - valorDesconto
valor = valorDesconto * 100

print("O valor do desconto é de", valor, "porcento")