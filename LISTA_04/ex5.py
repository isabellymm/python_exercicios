#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

num = []
num_par = []
num_impar = []


for i in range(0,20):
    num.append(int(input('Número '+ str(i+1) + ':\n')))

for valor in num:
    if valor % 2 ==0:
        num_par.append(valor)
    elif valor % 2 ==1:
        num_impar.append(valor)

print('Lista de todos os números : ',num)
print('Lista de números pares : ',num_par)
print('Lista de números impares :',num_impar)