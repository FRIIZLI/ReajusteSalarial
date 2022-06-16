'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

dia = int(input('Digite um número de 1 a 7 para saber o dia da semana correspondente: '))

if dia == 1:
    print('O número digitado {}, é referente a domingo.'.format(dia))
elif dia == 2:
    print('O número digitado {}, é referente a segunda-feira.'.format(dia))
elif dia == 3:
    print('O número digitado {}, é referente a terça-feira.'.format(dia))
elif dia == 4:
    print('O número digitado {}, é referente a quarta-feira.'.format(dia))
elif dia == 5:
    print('O número digitado {}, é referente a quinta-feira.'.format(dia))
elif dia == 6:
    print('O número digitado {}, é referente a sexta-feira.'.format(dia))
elif dia == 7:
    print('O número digitado {}, é referente a sábado.'.format(dia))
else:
    print('O número digitado é inválido.')