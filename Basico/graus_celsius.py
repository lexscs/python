#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.(fórmula C = 5 * ((F-32) / 9))

f = float(input('Digite a temperatura (Fº) para fazer a conversão para graus Celsius: '))
print('A temperatura convertida: %.2f' %(5/9 * (f-32)))
