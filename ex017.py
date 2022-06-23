'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

ano = int(input('Informe um ano para saber se ele é bissexto ou não. '))

if (ano % 4 == 0 and ano%100!=0) or (ano % 400 == 0):
    print('O ano {} é um ano bissexto.'.format(ano))
else:
    print('O ano {} não é um ano bissexto.'.format(ano))


