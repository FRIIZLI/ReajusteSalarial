'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido.'''

sexo = str(input('Informe o seu sexo: F para Feminino - M para Masculino.').upper())

if sexo == 'F':
    print('Sexo feminino.')
elif sexo == 'M':
    print('Sexo masculino.')
else:
    print('Sexo inválido.')
    