#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# "Telefonou para a vítima?" 
# "Esteve no local do crime?" 
# "Mora perto da vítima?" 
# "Devia para a vítima?" 
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
#   exemplo: res1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))

respostas_positivas = 0
pergunta1 = input("Você telefonou para a vítima?(S ou N): ")
if pergunta1 == "S":
    respostas_positivas = respostas_positivas + 1
else:
    respostas_positivas = respostas_positivas + 0

pergunta2 = input("Você esteve no local do crime?(S ou N):  ")
if pergunta2 == "S":
    respostas_positivas = respostas_positivas + 1
else:
    respostas_positivas = respostas_positivas + 0

pergunta3 = input("Você mora perto da vítima?(S ou N):  ")
if pergunta3 == "S":
    respostas_positivas = respostas_positivas + 1
else:
    respostas_positivas = respostas_positivas + 0

pergunta4 = input("Você devia para a vítima?(S ou N):  ")
if pergunta4 == "S":
    respostas_positivas = respostas_positivas + 1
else:
    respostas_positivas = respostas_positivas + 0

pergunta5 = input("Você já trabalhou com a vítima?(S ou N):  ")
if pergunta5 == "S":
    respostas_positivas = respostas_positivas + 1
else:
    respostas_positivas = respostas_positivas + 0

if respostas_positivas == 2:
    print("Classificação: Suspeito")

if respostas_positivas == 3 or respostas_positivas == 4:
    print("Classificação: Cúmplice")

if respostas_positivas == 5:
    print("Classificação: Assassino")
elif respostas_positivas == 0 or 1:
    print("Classificação: Inocente")