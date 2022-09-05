#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.


nome_usuario = (input("Informe nome do usuário :"))
senha = (input("Informe a senha :"))

while senha == nome_usuario:
    print("Erro: a senha não pode ser igual a o usuário")
    nome_usuario = (input("Informe nome do usuário :"))
    senha = (input("Informe a senha :"))
else:
    print("Cadastro feito com sucesso!")

print("Fim do programa")