#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite outro numero inteiro:'))
n3 = float(input('Digite outro numero agora real:'))

a1 = (n1 * 2) * (n2/2)
a2 = (n1**3) + n3
a3 = (n3**3)

# o produto do dobro do primeiro com metade do segundo .

print(f'O resultado da expressão, o produto do dobro do primeiro com metade do segundo é :{a1:.1f}')

# a soma do triplo do primeiro com o terceiro.

print(f'Resultado da expressão a soma do triplo do primeiro com o terceiro : {a2:.1f}')

#o terceiro elevado ao cubo.

print(f'Resultado do terceiro elevado ao cubo: {a3:.2f}')



