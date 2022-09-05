#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
#O usuário deve informar de qual numero ele deseja ver a tabuada

num = int (input("Digite um número : "))
cont = 1

while (cont<11):
    print(num,'x',cont,'=',num * cont)
    cont = cont + 1
     


    