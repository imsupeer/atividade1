#Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
# Álcool: 
#   até 20 litros, desconto de 3% por litro 
#   acima de 20 litros, desconto de 5% por litro 
# b) Gasolina: 
#   até 20 litros, desconto de 4% por litro 
#   acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
# seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
# que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

quantidade_de_litros = float(input("Insira a quantidade de litros que deseja: "))
tipo_de_combustivel = input("Insira o tipo de combustível:(A-álcool ou G-gasolina): ")

if tipo_de_combustivel == "A":
    preco = quantidade_de_litros * 1.90
    if quantidade_de_litros <= 20:
        preco = quantidade_de_litros * 1.90 - 3/100
    else:
        preco = quantidade_de_litros * 1.90 - 5/100

if tipo_de_combustivel == "G":
    preco = quantidade_de_litros * 2.50
    if quantidade_de_litros <= 20:
        preco = quantidade_de_litros * 2.50 - 4/100
    else:
        preco = quantidade_de_litros * 2.50 - 6/100 

print(f"O valor total a ser pago é: R${preco}")