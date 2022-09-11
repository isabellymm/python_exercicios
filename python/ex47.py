lista = []

while True:
    n = int (input("Digite os números [0] para sair do loop: "))
    if n == 0:
        break
    lista.append(n)
print ("O maior número da lista é : ",max(lista))

# [max] mostra o maior número em uma lista
# [min] mostra o menor númnero em uma lista
# [sum] soma os elementos de uma lista
# [len]  descobrindo tamanho de uma lista 
# [remove] remove um item da lista
# [append] adiciona um ou mais itens a uma lista 