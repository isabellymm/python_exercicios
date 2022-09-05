#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

print('Número fatorial (X!)')
num = int (input('Informe um número '))

result  = 1 
count = 1

while count  <= num:
   result  *=  count 
   count += 1 
print(result)



