aux = input("RM")
rm = int(aux)
soma = 0

resto = rm % 10
rm = rm // 10
soma = soma + resto

resto = rm % 10
rm = rm // 10
soma = soma + resto

resto = rm % 10
rm = rm // 10
soma = soma + resto

resto = rm % 10
rm = rm // 10
soma = soma + resto

resto = rm % 10
rm = rm // 10
soma = soma + resto

print(f"A soma vale {soma}") #f-string (f"texto {string}")