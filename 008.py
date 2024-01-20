#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

c = input('Colaborador digite seu nome :')
print (f'Seja bem vindo {c}') # Boas vindas

h = (float (input('Quantos você ganha por hora ?'))) # Ganho por horas
t = (float (input('Número de horas trabalhadas ?'))) #Trabalho por horas
mes = (float (input('Número de dias trabalhadas no mês ?'))) #Trabalho por mes

dia = h * t #Salario no dia
sal = dia * mes #Salario por mês

print (f'Seu salario por dia, {dia:.2f} e por mês é: {sal:.2f}')









