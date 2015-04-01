# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:53:00 2015

@author: Felipe e Gabriel
"""
import turtle
import random   #importa funçao que sorteia, escolhe aleatoriamente
import time


listalimpa=[]  
arquivo = open("entrada.txt",encoding="utf-8")
ler = arquivo.readlines()   #le as linhas do arquivo

for i in range(len(ler)):
    listalimpa.append(ler[i].strip().lower())  #transforma a escolhida em letra minuscula e separa as palavras
    print(listalimpa)
    s = random.choice(listalimpa)   #s = palavra sorteada
    print(s)

print(ler)

"""
acentos= dict()
acentos["a"]==ã==á==à
"""


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
k = 0
digitadas=[]
acertos=0

listaerros=[]
x=0  #palavras chutadas erradas
while k < tamanho:
    if s[k] == " ":
        acertos+=1
        
    k+=1
while True:
    
    escolha=window1.textinput("\nDigite uma letra:","\nDigite uma litra:").strip()
    digitadas.append(escolha)
    
    def usuario_venceu(escolha,s,digitadas):
        if digitadas in s:
            print("voce venceu!!")
            tartaruga3.penup()
            tartaruga3.setpos(100,110)
            tartaruga3.pendown()
            tartaruga3.write("VOCE VENCEU!!", True, font=("Arial",16))  
            

        return True 
        
        
        if escolha in digitadas:
            print("Voce ja escolheu essa letra!")
     
        if escolha in s:
            p=s.find(escolha)
            i=0
            m = s[i]
            
            
            if m == escolha:
                    tartaruga2.penup()
                    tartaruga2.setpos(-30+(i+1)*16, -97)
                    tartaruga2.pendown()
                    tartaruga2.write(escolha, font=("Arial", 16))
                    i+=1
                    acertos=+1
                    
            elif escolha == " ":
                    tartaruga2.penup()
                    tartaruga2.setpos(-30,+16(i+1),-97)
                    tartaruga.pendown()
                    tartaruga.write(s[i],font=("Arial",16))
                    i +=1
                    i = len(s)
        
            else:
                    x+=1
                    print("voce errou!")
                    i=len(s)


        else:
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
                time.sleep(3)
                tartaruga3.write("PARA JOGAR NOVAMENTE DIGITE SIM",(-100,-200),True,font=("Arial",16))
                #if escolha=("sim"):
                    #restart
                #break
        return(escolha,s,digitadas)
print(acertos)
print(digitadas)      
#  if acertos == len(s):
#     tartaruga3.penup()
 #    tartaruga3.setpos(100,110)
  #   tartaruga3.pendown()
   #  tartaruga3.write("VOCE VENCEU!!", True, font=("Arial",16))
