# Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos. Escreva um algoritmo que
# calcula a velocidade média em m/s e em km/h de um corredor, seu algoritmo recebe como dados de entrada a distância
# em metros e o tempo em segundos.

distancia = float(input("Qual a distância em metros?"))
segundos = float(input("Qual o tempo em segundos?"))

velocidadeMetros = distancia / segundos
velocidadeKm = velocidadeMetros * 3.6

print("A velocidade em M/s é de", int(velocidadeMetros),"e a velocidade em Km/h é de", velocidadeKm)
