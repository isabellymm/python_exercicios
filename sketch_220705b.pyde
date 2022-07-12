'''
size(400,400) #PONTOS
strokeWeight(6)
point(20,20)
point(30,30)
strokeWeight(4)
point(40,40)
point(50,50)
strokeWeight(2)
point(60,60)
point(70,70)
'''

'''
triangle(60,10,25,60,75,65) #TRIÂNGULOS
strokeWeight(1)
triangle(40,22,45,67,23,44)
strokeWeight(2)
triangle(22,54,56,88,66,54)
'''

'''
quad(38,56,21,45,59,54,20,10) #QUADRADO
#rect(15,15,40,50)
#rect(55,55,15,25)
'''

'''
ellipse(40,40,60,60) #large circle  #CIRCULOS
ellipse(75,75,32,32) #small circle

ellipse(40,40,60,30)
ellipse(75,75,12,32)
'''
'''
background(0) #COR DE FUNDO (0 -- 255)
fill(205)  # PREENCHIMENTO DE COR DE UMA FIG. (0 -- 255)
fill(250) #TRANSPARÊNCIA (255)
stroke(153) # COR DA BORDA 
noStroke(33,3,45,2) # SEM BORDA
smooth() #QUALIDADE DA LINA
noSmooth()  #  FIG. QUADRICULADA
'''
'''
size(400,440)
for i in range (20, 150 ,10) :
    line(i, 20 , i, 180)
'''
'''
noFill()
smooth()

for d in range(0 , 150 , 10) :
    ellipse(50, 50 , d ,d )
    
'''

'''
size(500,500)
strokeWeight(3)
smooth()

for y in range (10, 500 ,10) :
    for x in range ( 10 , 500 , 10,):
        point(x,y)
'''
'''
size(200, 200)
background(127)
noStroke()

for i in range (0, height , 20) :
    fill(0)
    rect(0 ,i , width , 10)
    fill(255)
    rect(i , 0, 10, height)
    
'''

'''
size(400,440)
for i in range (10, 300 ,5) :
    line(i, 10 , i, 150)
'''

'''
size (400,400)
altura = height/5 
y = 0

for i in range (200, width , 5 ) :
   line (i, y, i, y  + altura)
   
y = y + altura
for i in range (100, width , 10 ) :
   line (i, y, i, y  + altura)
   
   
y = y + altura
for i in range (75, width , 7 ) :
   line (i, y, i, y  + altura)
   
y = y + altura
for i in range (160, width , 10 ) :
   line (i, y, i, y  + altura)

y = y + altura
for i in range (100, width , 4) :
   line (i, y, i, y  + altura)
'''
#background (123,253,159)
#background(344,56,323)
#background(025,366,158)

'''
from random import*

size(400,400)

for i in range(1500):
    x = randrange(0,400)
    y = randrange(0,400)
    strokeWeight(randrange(0,250))
    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)
    stroke(r,g,b,randrange(0,255))
    point(x,y)
    
for i in range(100):
    x = randrange(0,400)
    y = randrange(0,400)  #POSTOS NA TELA DE FORMA ALEATÓRIA
    r = randrange(0,255)
    stroke(r,234,123)
    strokeWeight(5)
    point(x,y)

for i in range(100):
    x = randrange(0,400)
    y = randrange(0,400)
    strokeWeight(2)
    r = randrange(0,255)
    stroke(r, 200, r, randrange (0,255)
    point(x,y)    
            
 '''    
 x = 0

def setup():
    size(400,400)
    
def draw():
    global x
    fill(255,10)
    rect(0,0,400,400)
    strokeWeight(5)
    point(mouseX,mouseY)
    #point(x,30)
    #x = x + 2

 
