#Faça um Programa que leia três números e mostre o maior deles.

x = int (input("Insira um número:"))
y = int (input("Insira um número:"))
z = int (input("Insira um número:"))

maior = x

if (y > maior):
        maior = y
if (z > maior):
        maior = z

print('Maior: ',maior)