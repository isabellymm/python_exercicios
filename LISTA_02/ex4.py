#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

carc = str (input("Digite um caractere:"))

if carc =='a' or carc =='e' or carc =='i' or carc =='o' or carc =='u' or \
   carc =='A' or carc =='E' or carc =='I' or carc =='O' or carc =='U':
   print ("O caracter digitado é uma volgal")
else: 
   print("O caracter digitado é uma consoante")