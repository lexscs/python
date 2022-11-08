#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


import math

raio = float(input('Digite o valor do raio: '))
circulo = 2 * math.pi * raio
print("O valor do raio: {:.3f}".format(circulo))