'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = str(input('Informe o turno que você estuda.\nM-para turno matutino, V-para turno vespertino, N-noturno para turno: ').upper())

if turno == "M":
    print('Turno matutino, Bom dia!')
elif turno == "V":
    print('Turno vespertino, Boa tarde!')
elif turno == "N":
    print('Turno noturno, Boa noite!')
else:
    print('Valor inválido!')




