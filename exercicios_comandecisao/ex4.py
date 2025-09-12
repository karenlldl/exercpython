# A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha
# trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra.
# O valor da hora-extra é o valor que ele recebe por hora acrescido de 50%. 
# Supondo que ele trabalhe apenas nos dias úteis, escreva um algoritmo que recebe:
# a) o total de dias úteis de um mês
# b) o total de horas trabalhadas pelo trabalhador
# c) quanto o trabalhador recebe por hora
# Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário final
# do trabalhador.

dias = int(input("Digite o total de dias trabalhados no mês: "))
horasTrabalhadas = float(input("Quantas horas trabalhadas no mês?"))
recHora = float(input("Quanto recebe por hora?"))

horasPadrao = 8 * dias

if horasTrabalhadas > horasPadrao:
    horaExtra = horasTrabalhadas - horasPadrao
    salarioExtra = horaExtra * recHora * 1.5
    salarioPadrao = horasPadrao * recHora
    salarioTotal = salarioPadrao + salarioExtra
    print("Voce trabalhou", horaExtra, " horas extras e teve um acrescimo no salario de: ", salarioExtra, ". Seu salario final e:", salarioTotal)
else:
    salarioNormal = horasTrabalhadas * recHora
    print("Você nao fez horas extras e seu salario é de", salarioNormal)


