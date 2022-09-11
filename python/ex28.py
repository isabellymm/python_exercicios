
print ("Responder com [1][para sim] ou [0][para não]   ")
print()
pergunta1 = str (input("Telefonou para a vítima? ") )
pergunta2 = str (input("Esteve no local do crime? "))
pergunta3 = str (input("Mora perto da vítima? "))
pergunta4 = str (input("Devia para a vítima? "))
pergunta5 = str (input("Já trabalhou com a vítima? "))

#perguntas = pergunta1 + pergunta2  + pergunta3  + pergunta4  + pergunta5 

#resp = suspeito = "S"
#inocente = "I"

if pergunta1 == 1:
   resp = "S1"

elif  pergunta2 == 1:
 resp = "S2"

elif  pergunta3 == 1:
 resp = "S3"


elif  pergunta4 == 1:
 resp = "S4"


elif  pergunta5 == 1:
 resp = "S5"


if pergunta1 == 0:
 resp = "I1"

elif pergunta2 == 0:
 resp = "I2"

elif pergunta3 == 0:
 resp = "I3"

elif pergunta4 == 0:
 resp = "I4"

elif pergunta5 == 0:
 resp = "I5"

resposta = int
a = "S1", "S2" , "S3" , "S4" ,"S5"
b =  "S2" , "S3" , "S4" ,"S5"
c =  "S3" , "S4" ,"S5"
d = "S4" ,"S5"
e = "S5"


if resposta == a and b and c and d and e:
    print("Assasino")

elif resposta == a and b and c:
    print("Cúmplice")

elif resposta == a and b:
    print("Suspeito")


