'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''
numero = int(input('Insira um número de 0 a 10: '))
while 0 > numero or 10 < numero:
    numero = int(input('Somente números entre 0 e 10: '))

