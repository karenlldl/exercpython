valorAvista = float(input("Digite o valor do IPTU a vista: "))
parcelado = float(input("Digite o valor de cada parcela: "))

diferenca = parcelado * 10

valorDesconto = diferenca / valorAvista

print("O valor do desconto é de", int(valorDesconto), "porcento")
