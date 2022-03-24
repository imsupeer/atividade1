#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.

valor_mq = int(input("Insira o total de área a ser pintada(em m²): "))
litros = valor_mq / 3

if valor_mq % 54 == 0:
	latas = valor_mq / 54
else: 
	latas = int(valor_mq / 54) + 1

valor_total = latas * 80
print(f"O total de latas a ser utilizado é: {latas} e o valor total será: R${valor_total}")