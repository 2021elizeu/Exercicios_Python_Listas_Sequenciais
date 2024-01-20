#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

i = float(input('Digite sua altura :'))



ph = (72.7*i)-58
pm = (62.1*i)-44.7

print (f'Sua altura ideal é para homem: {ph:.2f} e para mulher {pm:.2f}.')
