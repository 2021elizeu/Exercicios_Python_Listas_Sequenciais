"""Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math

print('Obs: cada 1 Lts para 3 mtr de área')

f = float(input('Qual a área em metros:'))#Pergunta ao cliente

c = (f * 3)/18 #calculo de quantidades latas de tintas

print(f'Quantidade de latas de tintas de 18 lts: {c:.1f}')

p = c * 80 #calculo do custos

print(f'Custo Total R$ {p:.2f}')



