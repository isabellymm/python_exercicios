def Triangulo():
    lado1 = float (input("Informe o lado do triãngulo :"))
    lado2 = float (input("Informe o lado do triãngulo:"))
    lado3 = float (input("Informe o lado do triãngulo:"))
    
    if lado1 == lado2 == lado3:
        print( "O Triangulo é Equilátero")
    
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
       print( "O Triangulo é  Isósceles")
    
    elif lado1 != lado2 != lado3:
        print("Triangulo é Escaleno")
    
print(Triangulo())