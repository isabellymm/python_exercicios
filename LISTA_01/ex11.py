#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.



x = int (input("Informe um número:"))
y = int (input("informe um número:"))
z = float (input("Informe un número do tipo float(real):"))

a = ((x * 2) + y/2)
b = ((x * 3) + z)
c = (z ** 3)

print (a)
print (b)
print (c)