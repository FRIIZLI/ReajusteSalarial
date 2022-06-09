'''Faça um Programa que leia três números e mostre o maior deles.'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O maior número é {}.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior número é {}.'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O maior número é {}.'.format(n3))
elif n1 == n2 == n3:
    print('Os três números são iguais.')


