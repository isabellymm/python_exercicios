num = []
qtd = int (input("Informe a quantidade de números : "))

for n in range(0,int(qtd)):
    num.append(int(input("Dgite o número : ")))

soma_num = sum(num)
print("A soma dos números é de : ", soma_num)