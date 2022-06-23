'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E'''

nota1 = float(input('Informe a sua primeira nota: ').replace(',','.'))
nota2 = float(input('Informe a sua segunda nota: ').replace(',','.'))
media = (nota1 + nota2) / 2

if media >= 9.0:
    print('A sua primeira nota é {} e a sua segunda nota é {}\nA sua média é {} e seu conceito "A", APROVADO.'.format(nota1, nota2, media))
elif media >= 7.5:
    print('A sua primeira nota é {} e a sua segunda nota é {}\nA sua média é {} e seu conceito "B". APROVADO'.format(nota1, nota2, media))
elif media >= 6.0:
    print('A sua primeira nota é {} e a sua segunda nota é {}\nA sua média é {} e seu conceito "C". APROVADO'.format(nota1, nota2, media))
elif media >= 4.0:
    print('A sua primeira nota é {} e a sua segunda nota é {}\nA sua média é {} e seu conceito "D". REPROVADO'.format(nota1, nota2, media))
elif media <= 4.0:
    print('A sua primeira nota é {} e a sua segunda nota é {}\nA sua média é {} e seu conceito "E". REPROVADO'.format(nota1, nota2, media))
else:
    print('Valor digitado inválido.')
