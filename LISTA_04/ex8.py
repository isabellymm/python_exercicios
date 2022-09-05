#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
#Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
alt = []

for i in range(5):
    idade.append(int(input('Informe a sua idade : \n ')))
    alt.append(float(input('Informe a sua altura : \n  ')))

print(idade[:: -1])
print(alt[:: -1])  

