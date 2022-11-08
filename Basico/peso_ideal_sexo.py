''' Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 '''

h = float(input('Digite a altura da pessoa(h): '))
sexo = input('Digite o sexo da pessoa (h)homem ou (m)mulher:')
if sexo == 'h':
    pesoIdeal = print('O peso ideal do homem é: ', (72.7*h) - 58)
else:
    pesoIdeal = print('O peso ideal da mulher: ', (62.1*h) - 44.7)
    
