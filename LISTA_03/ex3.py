#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


nome = str (input("Informe o nome do usuário : "))
idade = int (input("Informe a idade : "))
salário = float (input("Informe o salário : "))
sexo = str (input("Informe o sexo [F] ou [M] : "))
estado_civil = str  (input("Informe o seu estado cívil [S] , [C] , [V] , [D]  : "))

if 3 < len(nome):
    print(f"O nome {nome} é válido!")
else:
    print("Erro: O nome precisa ter mais de 3 caracteres")

if idade < 0:
    print("Erro: a idade não suportada")

elif idade > 150:
    print("Erro: a idade não suportada")

else:
    print(f"A idade é válida!")


if salário >= 0:
    print("Salário válido!")
else:
    print("Erro: salário menor que 0")


if sexo == "F" or sexo =="M":
    print("Sexo válido!")
else:
    print("Erro: usuário não ultizou [F] OU [M] ")


if estado_civil == "S" or estado_civil == "C" or estado_civil == "V" or estado_civil == "D":
    print("Estado Civil válido!")
else:
    print("Erro:  usuário não ultizou [S] , [C] , [V] , [D] ")