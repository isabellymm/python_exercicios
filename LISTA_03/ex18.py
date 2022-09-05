#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

num = []

qtn = int (input("informe a quantidade de números : "))



for n in range(0,int(qtn)):
    num.append(int(input("Dgite o número : ")))
    

maior = max(num)
menor = min(num)
soma = sum(num)

print('O maior número é :',maior )
print('O menor número é :',menor )
print('A soma dos números é :',soma)