'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
 seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Informe o salário do colaborador: R$ ').replace(',','.'))

if salario <= 280:
    reajuste = salario + (salario * 0.20)
    print('Para um salário de R$ {}, o reajuste será de 20% de aumento.\nO novo salário será de R$ {}.'.format(salario,reajuste))
elif salario > 280 <=700:
    reajuste = salario + (salario * 0.15)
    print('Para um salário de R$ {}, o reajuste será de 15% de aumento.\nO novo salário será de R$ {}.'.format(salario,reajuste))
elif salario > 700 <=1500:
    reajuste = salario + (salario * 0.10)
    print('Para um salário de R$ {}, o reajuste será de 10% de aumento.\nO novo salário será de R$ {}.'.format(salario,reajuste))
elif salario > 1500:
    reajuste = salario + (salario * 0.5)
    print('Para um salário de R$ {}, o reajuste será de 5% de aumento.\nO novo salário será de R$ {}.'.format(salario,reajuste))
else:
    print('Valor inválido.')



