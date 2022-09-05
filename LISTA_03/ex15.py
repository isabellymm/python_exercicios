#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


def fibonacci (n):
    if n in {0 , 1 }:
        return n 
    return fibonacci ( n - 1) + fibonacci ( n - 2)

def menu():
    n = int (input('Exibir ate o termo (maior que 2): '))


    for val in range ( 1 , n+1):
      print(fibonacci(val))


while True:
    menu()

