#Faça um Programa que leia três números e mostre o maior e o menor deles.


x = int (input("Insira um número:"))
y = int (input("Insira um número:"))
z = int (input("Insira um número:"))

maior = x

if (y > maior):
        maior = y
if (z > maior):
        maior = z

print('Maior: ',maior)

menor = x

if (y < menor):
        menor = y
if (z < menor):
        menor = z

print('Menor: ',menor)
