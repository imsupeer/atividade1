#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_do_arquivo = float(input("Insira o tamanho do arquivo(em MB): "))
velocidade_de_download = int(input("Insira a velocidade de sua internet(em Mbps): "))
tempo_estimado = (tamanho_do_arquivo/velocidade_de_download)/60

print(f"O tempo estimado para concluir o download é: {tempo_estimado}m")