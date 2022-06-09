'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.'''

produto1 = float(input('Digite o preço do primeiro produto: R$ ').replace(',','.'))
produto2 = float(input('Digite o preço do segundo produto: R$ ').replace(',','.'))
produto3 = float(input('Digite o preço do terceiro produto: R$ ').replace(',','.'))

if produto1 < produto2 and produto1 < produto3:
    print()
    print('O produto com melhor preço é o primeiro produto\ncom o valor de R$ {}.'.format(produto1))
elif produto2 < produto1 and produto2 < produto3:
    print()
    print('O produto com melhor preço é o segundo produto\ncom o valor de R$ {}.'.format(produto2))
elif produto3 < produto1 and produto3 < produto2:
    print()
    print('O produto com melhor preço é o terceiro produto\ncom o valor de R$ {}.'.format(produto3))
else:
    print()
    print('Os três produtos tem preços iguais.')