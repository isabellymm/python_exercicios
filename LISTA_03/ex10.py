#Faça um programa que receba dois números inteiros 
# e gere os números inteiros que estão no intervalo compreendido por eles.

a = int(input('Digite um número : '))
b = int (input('Digite um número maior : '))

if a > b:
    print("Erro: número há de ser menor ")


for a in range(a,b + 1):
    print(a)