#Altere o programa anterior para mostrar no final a soma dos números.

a = int(input('Digite um número : '))
b = int (input('Digite um número maior : '))
soma = 0 


if a > b:
    print("Erro: número há de ser menor ")


for a in range(a,b + 1):
    print(a)
    soma = soma + a
print('A soma dos números foi de',soma)