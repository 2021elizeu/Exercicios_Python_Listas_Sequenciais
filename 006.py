#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

r = float(input('Digite o raio em cm² :')) 
pi = 3.1415926
a = pi * ( r ** 2 )

print(f'A área do circulo é: {a:.2f} cm²')