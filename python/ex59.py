#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
#limitando o fatorial a números inteiros positivos e menores que 16.

print('Número fatorial (X!)')
num = int (input('Informe um número :'))


result = 1 
count = 1

while count  <= num:
   result  *=  count 
   count += 1 
   print(result)
num = int (input('Informe um número : '))
