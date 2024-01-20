"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
        Acrescente 10% de folga e sempre arredonde os valores para cima,
        isto é, considere latas cheias.
"""
import math

print('LOJA DE TINTAS BARTE-POÁ')
print('Para cada 1 lts 6 metros de rendimento')

a = (int(input('Qual a área em metros:')))#usuario digita a entrada

c0 = math.ceil (a/18) # Calculo da quantidade de galoes de 18lts
p0 = (c0 * 10)/100 # porcentagem 10 % 
q = math.ceil (p0 + c0) #Quantidade de total de galoes 
c1 = math.ceil (q * 80) # Calculo do custo 

d0 = math.ceil (a/3.6) #Calculo da quantidades de galoes 3.6 lts
p1 = (d0 * 10)/100 #Porcentagem 10%
q1 = math.ceil(p1 + d0) #Quantidade de galoes
d1 = math.ceil (q1 * 25) # Calculo do custo 

print(f'Quantidades de galoes de 18 lts: {q:.1f} ')
print(f'Custo total galoes de 18 lts:  R$ {c1:.2f} ')
print(f'Quantidades de galoes de 3.6 lts {q1:.1f} ')
print(f'Custo total galoes de 3.6 lts R$ {d1:.2f}')

