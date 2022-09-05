#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

num = 1
par = 0 
impar = 0 

for i  in range(10) :
    num = int  (input('Digite 10 números inteiros : '))

    if num % 2 == 0 :
        #num = par
        par = par + 1 
    else :
        num = impar 
        impar = impar + 1 

print ("A quantidade  de números pares é de :",par)

print ("A quantidade  de números impar  é de :",impar )

