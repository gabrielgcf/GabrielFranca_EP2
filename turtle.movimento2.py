import turtle
import random   #importa funçao que 



listalimpa=[]
arquivo = open("entrada.txt",encoding="utf-8")
ler = arquivo.readlines()

for i in range(len(ler)):
    listalimpa.append(ler[i].strip().lower())
    print(listalimpa)
    s = random.choice(listalimpa)   #s = palavra sorteada
    print(s)

print(ler)

tamanho = len(s)
for i in range(len(s)):
    if s[i]==" ":
        tartaruga2.penup()
        tartaruga2.setpos(-30+(i+1)*16,-150)
        tartaruga2.write(" ",False, font=("Arial", 20))
    else:
        tartaruga2.penup()
        tartaruga2.setpos(-25+(i+1)*16,-100)
        tartaruga2.write("_",False,font=("Arial",20))





window1 = turtle.Screen()

window1.bgcolor("blue")
window1.title("O JOGO DA FORCA")

tartaruga = turtle.Turtle()
tartaruga2 = turtle.Turtle()

def desenhaforca():
    tartaruga.setpos(0,0)
    tartaruga.back(200)
    tartaruga.left(90)
    tartaruga.fd(250)
    tartaruga.right(90)
    tartaruga.fd(125)
    tartaruga.right(90)
    tartaruga.fd(50)
    
desenhaforca()

tamanho = len(s)
for i in range(len(s)):
    if s[i]==" ":
        tartaruga2.penup()
        tartaruga2.setpos(-30+(i+1)*16,-150)
        tartaruga2.write(" ",False, font=("Arial", 20))
    else:
        tartaruga2.penup()
        tartaruga2.setpos(-25+(i+1)*16,-100)
        tartaruga2.write("_",False,font=("Arial",20))




def desenhacabeca():
    tartaruga.right(90)
    tartaruga.circle(25)  
    

if x == 1:               #x = quantos erros
    desenhacabeca()

def desenhatronco():
    tartaruga.up()
    tartaruga.left(90)
    tartaruga.fd(50)
    tartaruga.pendown()
    tartaruga.fd(75)

if x == 2:
    desenhatronco()

def desenhabraço1():
    
    tartaruga.back(50)
    tartaruga.left(60)
    tartaruga.fd(60)
    tartaruga.back(60)

if x == 3:   
    desenhabraço1()

def desenhabraço2():
    tartaruga.right(120)
    tartaruga.fd(60)
    tartaruga.back(60)
    tartaruga.left(60)
if x == 4:
    desenhabraço2()

def desenhaperna1():
    tartaruga.fd(50)
    tartaruga.left(45)
    tartaruga.fd(40)
    tartaruga.back(40)
    tartaruga.right(45)

if x == 5:    
    desenhaperna1()

def desenhaperna2():
    tartaruga.right(45)
    tartaruga.fd(40)

if x == 6:    
    desenhaperna2()
    