"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
nome = input('Digite seu nome :') #entrada do nome
print(input(f'{nome} , seja bem vindo !!!')) #boas vindas ao cliente

valor = float(input('Seu salario por hora é R$: ')) #digitar o salario por hora
horas = float(input('Quantas horas trabalha por dia: ')) #horas do sia trabalhado 
mes = float(input('Quantos dias trabalha por mês: ')) #dias trabalha por mes
total = (valor * horas) * mes
ir = total * (11/100)
inss = total * (8/100)
sindicato = total * (5/100)
liquido = total - ir - inss - sindicato


print(f'Salario bruto R$ {total:.2f}  ')
print(f'IR R$ {ir:.2f} ')
print(f'INSS R$ {inss:.2f} ')
print(f'sindicato R$ {sindicato:.2f} ')
print(f'Valor Total Liquido R$ {liquido:.2f} ')








