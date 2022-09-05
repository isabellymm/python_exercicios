#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.


mult = 0

print('==' * 15 + 'NÚMEROS PRIMOS' + '==' * 15)
num_primo = int(input('Infrome um número : '))

for count in range(2,num_primo):
    if (num_primo % count == 0):
        mult += 1


if mult ==0:
    print('O número é primo!')

else:
    print('O número não é primo!')



