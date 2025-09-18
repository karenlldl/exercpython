print("Resolvendo equações da forma ax2 + bx + c = 0")
import math
a = float(input("A:"))
b = float(input("B:"))
c = float(input("C:"))

if a == 0:
    print("Não é uma equação de segundo grau!")
else:
    delta = b * b - 4 * a * c
    if delta >= 0:
        x1 = (- b + math.sqrt(delta)) / (2 * a)
        x2 = (- b - math.sqrt(delta)) / (2 * a)
        print(f"As raizes sao {x1} e {x2}")
    else:
        print("Delta é negativo logo a equacao nao possui raizes reais")