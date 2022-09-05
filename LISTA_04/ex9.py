#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e  mostre a soma dos quadrados dos elementos do vetor.

vetor_A = []
mapvetor_A = []

for i in range(3):
    vetor_A.append(int (input('Informe O '+ str(i+1) + 'º' ' número interiro : ' '\n' )))

mapvetor_A = list(map(lambda x : x * x, vetor_A))

print('quadrados dos elementos é de :',mapvetor_A)
print('A soma dos quadrados dos elementos do vetor : ',sum(mapvetor_A))