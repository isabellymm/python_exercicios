#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import numpy 


Lista = []
for i in range(5):
    Lista.append(int (input('Informe O '+ str(i+1) + 'º' ' número interiro : ' '\n' )))

result = numpy.prod(Lista)
print('A multiplicação dos números é de :',result)
print('A soma dos números é de :',sum(Lista))
