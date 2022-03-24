#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido.

pagamento_por_hora = float(input("Insira o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Insira o valor de horas trabalhadas por mês: "))

salario_bruto = pagamento_por_hora * horas_trabalhadas
imposto = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
salario_liquido = salario_bruto - imposto - inss - sindicato

print(f"Salário bruto: R${salario_bruto}")
print(f"Imposto: R$-{imposto}")
print(f"INSS: R$-{inss}")
print(f"Sindicato: R$-{sindicato}")
print(f"Salário líquido: R${salario_liquido}")