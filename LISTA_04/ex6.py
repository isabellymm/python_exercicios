#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
#imprima o número de alunos com média maior ou igual a 7.0.

count = 0
ListaNotas = []
Lista_Alunos = []
Notas_Alunos = []

for i in range(10):
    media = 0
    Notas_Alunos = []
    Lista_Alunos.append(str(input('Aluno : ')))

    for x in range(4):
        Notas_Alunos.append(float(input('Nota: ' + str(x+1) + '\n')))
        media += Notas_Alunos[x]
        
    
    media = media / 4
    ListaNotas.append(media)
    

    for n in range(1):
        if media >= 7:
            count += 1
            print('A média do aluno foi de : ',media, '\n')
        else:
            print('Aluno com média < que 7 : ',media, '\n')

print('O números de alunos com média maior do que 7 são : ',count)






