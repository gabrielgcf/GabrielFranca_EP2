import turtle
import random   #importa funçao que sorteia, escolhe aleatoriamente



listalimpa=[]  
arquivo = open("entrada.txt",encoding="utf-8")
ler = arquivo.readlines()   #le as linhas do arquivo

for i in range(len(ler)):
    listalimpa.append(ler[i].strip().lower())  #transforma a escolhida em letra minuscula e separa as palavras
    print(listalimpa)
    s = random.choice(listalimpa)   #s = palavra sorteada
    print(s)

print(ler)


acentos= dict()
acentos["a"]==ã==á==à



window1 = turtle.Screen()

window1.bgcolor("blue")
window1.title("O JOGO DA FORCA")

tartaruga = turtle.Turtle()
tartaruga2 = turtle.Turtle()
tartaruga3 = turtle.Turtle()

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
        tartaruga2.setpos(-60+(i+1)*16,-150)
        tartaruga2.write(" ",False, font=("Arial", 20))
    else:
        tartaruga2.penup()
        tartaruga2.setpos(-30+(i+1)*16,-100)
        tartaruga2.write("_",False,font=("Arial",20))

#aqui

digitadas=[]
acertos=0
lista= []
listaerros=[]
x=0  #palavras chutadas erradas
while True:
    
    escolha=window1.textinput("\nDigite uma letra:","\nDigite uma litra:").strip()
    digitadas.append(escolha)
    if escolha in digitadas:
        print("Voce ja escolheu essa letra!")
    if escolha in s:
        p=s.find(escolha)
        print("Voce acertou!")
    elif escolha not in s:
        print("Voce errou!")
        
            

    for i in range(len(s)):
        if escolha ==s[i]:
            tartaruga2.penup()
            tartaruga2.setpos(-30+(i+1)*16, -97)
            tartaruga2.pendown()
            tartaruga2.write(escolha, font=("Arial", 16))



    if escolha not in s:
        x+=1
        listaerros.append(escolha)
        #listaerros.write(font=("Arial",20))
        print("voce errou!")
        
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
            tartaruga3.write("VOCE PERDEU!!",True,font=("Arial",16))
            tartaruga3.write("PARA JOGAR NOVAMENTE DIGITE SIM",(-100,-200),True,font=("Arial",16))
            #if escolha=("sim"):
                #restart
            break
            
            
        