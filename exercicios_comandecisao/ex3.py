#Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma partida.
#Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a palavra EMPATE.

time_1 = int(input("Digite a quantidade de gols do time 1: "))
time_2 = int(input("Digite a quantidade de gols do time 2: "))

if time_1 > time_2:
    print("Time 1 ganhou!")
elif time_1 < time_2:
    print("Time 2 ganhou!")
else:
    print("Empate")