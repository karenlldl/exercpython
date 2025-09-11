# Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula e mostra 
# o valor do desconto e o novo preço do produto dado o percentual. 

produto = float(input("Digite o preço do produto: "))
percentual = float(input("Qual o percentual de desconto do produto?"))

porcentagem = 1 - percentual / 100
valorComDesconto = produto * porcentagem

porcentagemAum = 1 + percentual / 100
valorAum = produto * porcentagemAum

print("O desconto era de", percentual, "% o novo valor do produto é", valorComDesconto)
print("O aumento era de", percentual, "% o novo valor do produto é", valorAum)