#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.


num1 = float (input("informe um número:"))

num2 = float (input("informe um número:"))

conta = ""

print("---------------------------------")
print("[1] ------------- +")
print("[2] ------------- -")
print("[3] ------------- *")
print("[4] ------------- /")
print("---------------------------------")
operacao = int (input("Informe o tipo de Operação:"))

if operacao == 1:
    conta  =  (num1 + num2 )
    print(conta)

if (conta %2 ==  0):
    print("Esse número é Par!")

else:
    print("Esse número é Impar!")

if  conta > 0:
    print("Esse número é positivo!")

if conta < 0:
    print("Esse número é negativo!")

if conta == round(conta):
    print("Inteiro")

else:
    print("Decimal")




if (operacao == 2):
    conta = (num1 - num2)
    print(conta)

if (conta %2 ==  0):
    print("Esse número é Par!")

else:
    print("Esse número é Impar!")

if  conta > 0:
    print("Esse número é positivo!")

if conta < 0:
    print("Esse número é negativo!")

if conta == round(conta):
    print("Inteiro")

else:
    print("Decimal")





if operacao == 3:
    conta = (num1 * num2)
    print(conta)

if (conta %2 ==  0):
    print("Esse número é Par!")

else:
    print("Esse número é Impar!")

if  conta > 0:
    print("Esse número é positivo!")

if conta < 0:
    print("Esse número é negativo!")

if conta == round(conta):
    print("Inteiro")

else:
    print("Decimal")




if operacao == 4:
    conta = (num1 / num2)
    print(conta)

if (conta %2 ==  0):
    print("Esse número é Par!")

else:
    print("Esse número é Impar!")

if  conta > 0:
    print("Esse número é positivo!")

if conta < 0:
    print("Esse número é negativo!")

if conta == round(conta):
    print("Inteiro")

else:
    print("Decimal")
