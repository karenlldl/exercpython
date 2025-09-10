# Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual de aumento. 
# Você deverá escrever um algoritmo que recebe 2 números reais representando os salários antes e depois do 
# aumento e deverá calcular e exibir o percentual de aumento que João obteve.

salarioAntes = float(input("Digite o sálario antes do aumento: "))
salarioDepois = float(input("Digite o salário pós aumento: "))

aumento = salarioDepois - salarioAntes
salarioNovo = (aumento * 100) / salarioAntes

print("O aumento foi de",aumento,"ou seja", int(salarioNovo), "porcento")
