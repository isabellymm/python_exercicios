#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
#imprima o número de alunos com média maior ou igual a 7.0.

aluno = []
notas = []
notas_alunos = []
media = 2

for i in range(2):

    
    notas = []
    aluno.append(str(input('Aluno : ')))
    #print('Aluno '+ str(i+1) + ':\n')
    
    
    for c in range(2):
       notas.append(float(input('Nota: ' + str(c+1) + '\n')))
       
       for x in range(c):
        medias_alunos = sum(notas) / media
        print('A média do aluno foi de : ',medias_alunos)
        dicio_info = dict.fromkeys(aluno , medias_alunos)


            
        if medias_alunos >= 7 :
            dicio_info = dict.fromkeys(aluno , medias_alunos)
            #l1 = list(dicio_info.items())
            print('Alunos com média maior ou igual a 7.0 ',dicio_info)
            
            





#media = notas / 4
#notas_alunos.append(media)
#print(notas_alunos)
 