'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a - par ou ímpar;
b - positivo ou negativo;
c - inteiro ou decimal.'''

n1 = float(input('Digite um número: ').replace(',','.'))
n2 = float(input('Digite outro número: ').replace(',','.'))
operação = str(input('Escolha qual operação você deseja.\n(a) = par ou ímpar.\n(b) = positivo ou negativo.\n(c) = inteiro ou decimal. '))

if operação == "a":
    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Os números {} e {} são números pares.'.format(n1,n2))
    elif n1 % 2 == 0 and n2 % 2 != 0:
        print('O número {} é par e o número {} é ímpar.'.format(n1,n2))
    elif n1 % 2 != 0 and n2 % 2 == 0:
        print('O número {} é impar e o número {} é par.'.format(n1,n2))
    else:
        print('Os números {} e {} são números ímpares.'.format(n1,n2))
elif operação == "b":
    if n1 > 0 and n2 > 0:
        print('Os números {} e {} são positivos.'.format(n1,n2))
    elif n1 > 0 and n2 < 0:
        print('O número {} é positivo e o número {} é negativo.'.format(n1,n2))
    elif n1 < 0 and n2 > 0:
        print('O número {} é negativo e o número {} é positivo.'.format(n1,n2))
    else:
        print('Os números {} e {} são negativos.'.format(n1,n2))
elif operação == "c":
    if (n1 // 1) == n1 and (n2 // 1) == n2:
        print('Os números {} e {} são inteiros.'.format(n1,n2))
    elif (n1 // 1) == n1 and (n2 // 1) != n2:
        print('O número {} é inteiro e o número {} é decimal.'.format(n1,n2))
    elif (n1 // 1) != n1 and (n2 // 1) == n2:
        print('O número {} é decimal e o número {} é inteiro.'.format(n1,n2))
    else:
        print('Os números {} e {} são decimais.'.format(n1,n2))
else:
    print('Valor inválido.')

