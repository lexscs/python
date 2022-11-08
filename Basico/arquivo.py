'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

arquivo = float(input('Qual o tamanho do arquivo para download (em MB): '))
velocidade = float(input('Qual a velocidade do link de internet (em Mbps): '))

print('Tempo estimado para download: %.0f minutos ' %((arquivo / velocidade) * 60))