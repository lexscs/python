#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input('Digite o valor do salário/hora(R$): '))
numeroHoras = float(input('Digite a quantidade de horas trabalhadas: '))
salarioMes = salarioHora * numeroHoras
print('O seu salário do mês é: R$', salarioMes)