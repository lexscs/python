'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

metros = int(input('Informe a area a ser pintada: '))
litros = metros / 3
precoL = 80.00
capacidadeL = 18
latas = litros / capacidadeL
total = latas * precoL
print ('Você usará %.2f' %latas, 'latas de tinta')
print ('O preço total dos produtos R$: %.2f' %total)
