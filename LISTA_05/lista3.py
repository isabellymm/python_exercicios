
lista1 = [1, 2, 3, 4, 5]
numbers = [6, 7, 8, 9, 10]


print('Lista 1 : ',lista1)
print('Lista 2 : ',numbers, '\n')


cont = len(numbers) - 1
newList = []

while (cont >= 0):
    newList.append(numbers[cont])
    cont = cont - 1

print('Resultado : \n  ')

x = 0
for i in lista1:
    print("{}\t\t{}\t\t".format(lista1[x], newList[x]))
    x+=1
