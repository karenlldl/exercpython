#Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva um algoritmo
#que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo deverá ler o número
#de camisas, o número de calças e o número de pares de sapato.

print("Bem vindo ao calculador de looks")

qntdCamisas = int(input("Quantas camisas você tem?"))
qntdCalcas = int(input("Quantas calças você tem?"))
qntdSapatos = int(input("Quantos pares de sapato você tem?"))

variacoes = qntdCamisas * qntdCalcas * qntdSapatos

print("Ele pode se vestir de", variacoes, "maneiras diferentes.")
