#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float (input("Informe o sálario:"))

if (salario == 0):
    print("ERRO")

elif (salario <= 280):
    percentual = 20

elif (salario <= 700):
   percentual = 15

elif (salario <= 1500):
    percentual = 10
     
elif (salario >1500):
    percentual = 5

reajuste = salario * (percentual/100)
aumento = (salario + reajuste)


print()
print()
print("--------------------------------------------")
print("-------------------TABELA-------------------")
print("O salário antes do reajuste era de:  R$",salario)
print("O percentual de aumento aplicado é de:",percentual,"%")
print("O valor do aumento foi de:  R$",reajuste)
print("O novo salário, após o aumento é: R$",aumento)
print("--------------------------------------------")
print()
print()

     