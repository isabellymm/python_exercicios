#Faça um Programa que leia três números e mostre-os em ordem decrescente.

from cgi import print_form


pri = int (input('Informe o primeiro número : '))
seg= int (input('Informe o segundo  número : '))
ter = int (input('Informe o terceiro número : '))



if (ter > seg ):
    aux = ter
    ter = seg 
    seg = aux

if (seg > pri):
    aux = seg 
    seg = pri
    pri = aux 

if (ter > seg):
    aux = ter 
    ter = seg
    seg = aux 

print(pri)
print(seg)
print(ter)


