#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
#são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3%
#para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
#(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 
# Desconto do IR: Salário Bruto até 900 (inclusive) - isento 
# Salário Bruto até 1500 (inclusive) - desconto de 5% 
# Salário Bruto até 2500 (inclusive) - desconto de 10% 
# Salário Bruto acima de 2500 - desconto de 20% 

pagamento_por_hora = float(input("Insira o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Insira o valor de horas trabalhadas por mês: "))

salario_bruto = pagamento_por_hora * horas_trabalhadas
fgts = (salario_bruto * 11) / 100
sindicato = (salario_bruto * 3) / 100

if salario_bruto <= 900:
    salario_liquido = salario_bruto - sindicato

elif salario_bruto > 900 and salario_bruto <=  1500:
    desconto_ir = (salario_bruto * 5) / 100
    salario_liquido = salario_bruto- desconto_ir - sindicato
 
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = (salario_bruto * 10) / 100
    salario_bruto = salario_bruto - desconto_ir - sindicato

else:
    desconto_ir = (salario_bruto * 20) / 100
    salario_liquido = salario_bruto - desconto_ir -sindicato

print(f"Salário bruto: R${salario_bruto}")
print(f"FGTS: R$-{fgts}")
print(f"Sindicato: R$-{sindicato}")
print(f"Salário líquido: R${salario_liquido}")
