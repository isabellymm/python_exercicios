
pais_a = float (input("Informe a população do País A : "))
taxa_a = float (input("Informe a taxa de crecimento do País A : "))
pais_b = float (input("Informe a população do País B : "))
taxa_b = float (input("Informe a taxa de crecimento do País B : "))
anos = 0 

#if pais_a >= pais_b:
    #print("Erro: País A precisa ser menor que País B ")

while pais_a >= pais_b:
    print("Erro: população do País A maior ou igual que população do País B")
    pais_a = float (input("Informe a população do País A : "))
    taxa_a = float (input("Informe a taxa de crecimento do País A : "))
    pais_b = float (input("Informe a população do País B : "))
    taxa_b = float (input("Informe a taxa de crecimento do País B : "))
    anos = 0 


while pais_a <= pais_b: 
    pais_a = pais_a + (pais_a * taxa_a)
    pais_b = pais_b + (pais_b * taxa_b)
    anos = anos + 1 
print("São necessários",anos,"anos para que País A ultrapasse País B!") 

print("Fim do Programa")