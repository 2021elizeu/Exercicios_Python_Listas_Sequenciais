#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
#deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) 
#e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
#e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.

p = int(input('Digite o peso em kg :'))

if (p >= 50): #Condicional de Se
    print('multa excedente por kg = R$ 4,00')

m =  p - 50 # calculo de multa por excesso 

t = m * 4.00 # calculo de valores.

print(f'Excesso {m:.2f} Kg.') 
print(f'Total de multa por excesso R$ {t:.2f}')



