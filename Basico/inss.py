'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato (5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.'''


salarioHora = float(input('Digite o valor do salário/hora(R$): '))
numeroHoras = float(input('Digite a quantidade de horas trabalhadas: '))
salarioBruto = salarioHora * numeroHoras
IR = salarioBruto * 11/100
INSS = salarioBruto * 8/100
sindicato = salarioBruto * 5/100

salarioLiquido = salarioBruto - IR - INSS - sindicato
print('O seu salário sem descontos: R$ %.2f ' %salarioBruto)
print('O desconto de IR é: R$ %.2f ' %IR)
print('O desconto de INSS é: R$ %.2f ' %INSS)
print('O desconto do sindicato é: R$ %.2f ' %sindicato)
print('O seu salário do mês é: R$ %.2f ' %salarioLiquido)