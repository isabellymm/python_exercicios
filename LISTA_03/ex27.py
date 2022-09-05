#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas 
#e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

#print('Número maxímo de alunos é de 40 por sala!')

print('Média de alunos por turma')

turma = []
alunos = []
max_alunos = 40
x = 1


turma= (int(input('Qual o número de total de turmas :')))

print('Informe a qtd de alunos por turma ')


for i in range(turma):
    alunos = (int(input('Turma ' + str(i+1) + ' : ')))
    while alunos_turma > 40:
        print('Número maxímo de alunos é de 40 por sala!')
        alunos_turma =(int(input('Turma ' + str(i+1) + ' : ')))

    alunos.append(alunos_turma)



   

media = sum(alunos) / turma 

print('A média de alunos por turma é :',media)