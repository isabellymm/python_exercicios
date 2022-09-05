#Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

qtn = int (input("informe a quantidade de números : "))

for n in range(0,int(qtn)):
    numeros.append(int(input("Dgite o número : ")))
    

soma_dos_numeros  = sum(numeros)
qtd_numeros = len(numeros)

media = soma_dos_numeros / qtd_numeros

print("A soma dos números é de : ",soma_dos_numeros)
print("A média dos números é de : ",media)