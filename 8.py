#Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o mais baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

codigo_mais_gordo = 0
codigo_mais_magro = 0
codigo_mais_alto = 0
codigo_mais_baixo = 0

massa_mais_gordo = 0
massa_mais_magro = 1000 

altura_mais_alto = 0
altura_mais_baixo = 5 

soma_das_massas = 0
soma_das_alturas = 0
quantidade_de_clientes = 0

while True:
    codigo = input("Digite o codigo do cliente: ")
    if codigo == "0":
        break

    quantidade_de_clientes += 1
    altura = float(input("Digite a altura do cliente(em m): "))
    massa = float(input("Digite o massa do cliente(em kg): "))

    soma_das_massas += massa
    soma_das_alturas += altura

    if altura > altura_mais_alto:
        altura_mais_alto = altura
        codigo_mais_alto = codigo

    if altura < altura_mais_baixo:
        altura_mais_baixo = altura
        codigo_mais_baixo = codigo

    if massa > massa_mais_gordo:
        massa_mais_gordo = massa
        codigo_mais_gordo = codigo

    if massa < massa_mais_magro:
        massa_mais_magro = massa
        codigo_mais_magro = codigo

media_das_alturas = soma_das_alturas / quantidade_de_clientes
media_das_massas = soma_das_massas / quantidade_de_clientes

print(f"O cliente mais alto é o: {codigo_mais_alto}, ele tem: {altura_mais_alto}m")
print(f"O cliente mais baixo é o: {codigo_mais_baixo}, ele tem: {altura_mais_baixo}m")
print(f"O cliente mais gordo é o: {codigo_mais_gordo}, ele tem: {massa_mais_gordo}kg")
print(f"O cliente mais magro é o: {codigo_mais_magro}, ele tem {massa_mais_magro}kg")
print(f"A média de altura dos clientes é de: {media_das_alturas}m")
print(f"A média de massa dos clientes é de {media_das_massas}kg")