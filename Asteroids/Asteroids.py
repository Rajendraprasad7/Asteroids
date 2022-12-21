
import pygame
import sys
import time
import winsound
import random
from tkinter import *
from tkinter.ttk import *

path="assests\\"
whiteasteroid=path+"whiteasteroid.png"
root=Tk()
icon=path+"spaceship.jpg"

def startgame():

    pygame.mixer.init()
    pygame.mixer.music.load(path+'ltheme.wav')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    
    pygame.init()
    
    screen=pygame.display.set_mode((800,600))
    
    pygame.display.set_caption("Asteroids")

    #VARIABLES

    gameover=False
    RED=(255,0,0)
    GREEN=(0,255,0)
    YELLOW=(255,255,0)
    WHITE=(255,255,255)
    BLUE=(0,0,128)
    controller=[400,500]
    control_size=50
    background=(0,0,0)
    BLUE=(0,0,255)
    enemypos1=[random.randint(0,800-control_size),0]
    enemypos2=[random.randint(0,800-control_size),0]
    enemypos3=[random.randint(0,800-control_size),0]
    enemypos4=[random.randint(0,800-control_size),0]
    enemypos5=[random.randint(0,800-control_size),0]
    enemypos6=[random.randint(0,800-control_size),0]
    enemypos7=[random.randint(0,800-control_size),0]
    clock=pygame.time.Clock()
    SPEED=10
    score=0
    bulposx=-1000
    bulposy=-1000
    bul2posx=-1000
    bul2posy=-1000
    bgx=0
    bgy=-3000
    spaceship=pygame.image.load(path+"spaceship.jpg")
    gamebg=pygame.image.load(path+"gamebg.jpg")
    obstacle=pygame.image.load(path+"asteroid.png")
    bomb=pygame.image.load(path+"bomb.jpg")
    bullet=pygame.image.load(path+"bullet.jpg")
    boss1=pygame.image.load(path+"boss1.jpg")
    dodge=path+"dodge.wav"
    outt=path+"out.wav"
    punch=path+"punch.wav"
    woosh=path+"Woosh.wav"
    p=0
    q=[0]
    z=0
    space=0
    bos1posx=0
    bos1posy=0
    touch=0
    balive=True
    damage=30
    hlt="||||||||||"
    font1=pygame.font.SysFont("conicsans",30,True,True)
    font2=pygame.font.SysFont("conicsans",100,True,True)
    font3=pygame.font.SysFont("conicsans",30,True,True)

    pygame.display.set_icon(spaceship)

    #DEFINED FUNCTIONS


    def collision(controller,enemypos):
        px=controller[0]
        py=controller[1]
        ex=enemypos[0]
        ey=enemypos[1]
        if ex>=px and ex<=px+control_size or px>=ex and px<=ex+50:
            if ey>=py and ey<=py+control_size or py>=ey and py<=ey+50:
                return True
        
    def bulhit(bulx,buly,enemypos):
        bx=bulx
        by=buly
        ex=enemypos[0]
        ey=enemypos[1]
        if bx>=ex and bx<=ex+50 or ex>=bx and ex<=bx+10:
            if by>=ey and by<=ey+50 or ey>=by and ey<=by+25:
                return True
    
    def bulfired(xcord,ycord):
        bulposx=xcord
        bulposy=ycord
        pygame.draw.rect(screen,(255,0,0),(bulposx,bulposy,10,25))
        screen.blit(bullet,(bulposx,bulposy))
        
    def bulfired(xcord,ycord):
        bul2posx=xcord
        bul2posy=ycord
        pygame.draw.rect(screen,(255,0,0),(bul2posx,bul2posy,10,25))
        screen.blit(bullet,(bul2posx,bul2posy))

    def bosshit(bossx,bossy,bulx,buly):
        if bossx>=bulx and bossx<=bulx+10 or bulx>=bossx and bulx<=bossx+15:
            if bossy>=buly and bossy<=buly+25 or buly>=bossy and buly<=bossy+75:
                return True

########################################################################  MAIN GAME LOOP ######################################################################################
    while not gameover:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()
                
            elif event.type==pygame.KEYDOWN:
                x=controller[0]
                y=controller[1]
                if event.key==pygame.K_p:
                    pausetext=font2.render('PAUSED',1,RED)
                    screen.blit(pausetext,(230,250))
                    pygame.display.update()
                    pygame.mixer.music.pause()
                    time.sleep(10)
                    pygame.mixer.music.unpause()
                    screen.fill(background)
                    screen.blit(gamebg,(bgx,bgy))
                    
                if event.key==pygame.K_LEFT:
                    winsound.PlaySound(dodge,winsound.SND_ASYNC)
                    x-=control_size
                elif event.key==pygame.K_RIGHT:
                    winsound.PlaySound(dodge,winsound.SND_ASYNC)
                    x+=control_size
                elif event.key==pygame.K_UP:
                    winsound.PlaySound(dodge,winsound.SND_ASYNC)
                    y-=control_size
                elif event.key==pygame.K_DOWN:
                    winsound.PlaySound(dodge,winsound.SND_ASYNC)
                    y+=control_size
                elif event.key==pygame.K_SPACE:
                    bulposx=x+35
                    bulposy=y-25
                    pygame.draw.rect(screen,(0,255,0),(bulposx,bulposy,10,25))
                    screen.blit(bullet,(bulposx,bulposy))
                    bulfired(bulposx,bulposy)

                    bul2posx=x+5
                    bul2posy=y-25
                    pygame.draw.rect(screen,(0,255,0),(bul2posx,bul2posy,10,25))
                    screen.blit(bullet,(bulposx,bulposy))
                    bulfired(bul2posx,bul2posy)
                    
                    pygame.display.update()
                controller=[x,y]
        screen.fill(background)

        screen.blit(gamebg,(bgx,bgy))
        
        #ASTEROIDS
        

        
        if enemypos1[1]<600:
            enemypos1[1]+=5
        else:
            enemypos1[0]=random.randint(0,750)
            enemypos1[1]=0
        if collision(controller,enemypos1):
            out=font2.render('GAME OVER!',1,RED)
            screen.blit(out,(170,250))
            pygame.display.update()
            gameover=True
            winsound.PlaySound(outt,winsound.SND_ASYNC)
        if bulhit(bulposx,bulposy,enemypos1):
            enemypos1[0]=random.randint(0,750)
            enemypos1[1]=0
            bulposx=-100
            bulposy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)
        if bulhit(bul2posx,bul2posy,enemypos1):
            enemypos1[0]=random.randint(0,750)
            enemypos1[1]=0
            bul2posx=-100
            bul2posy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)

            
        if enemypos2[1]<600:
            enemypos2[1]+=6
        else:
            enemypos2[0]=random.randint(0,750)
            enemypos2[1]=0
        if collision(controller,enemypos2):
            out=font2.render('GAME OVER!',1,RED)
            screen.blit(out,(170,250))
            pygame.display.update()
            gameover=True
            winsound.PlaySound(outt,winsound.SND_ASYNC)
        if bulhit(bulposx,bulposy,enemypos2):
            enemypos2[0]=random.randint(0,750)
            enemypos2[1]=0
            bulposx=-100
            bulposy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)
        if bulhit(bul2posx,bul2posy,enemypos2):
            enemypos2[0]=random.randint(0,750)
            enemypos2[1]=0
            bul2posx=-100
            bul2posy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)

            
        if enemypos3[1]<600:
            enemypos3[1]+=8
        else:
            enemypos3[0]=random.randint(0,750)
            enemypos3[1]=0
        if collision(controller,enemypos3):
            out=font2.render('GAME OVER!',1,RED)
            screen.blit(out,(170,250))
            pygame.display.update()
            gameover=True
            winsound.PlaySound(outt,winsound.SND_ASYNC)
        if bulhit(bulposx,bulposy,enemypos3):
            enemypos3[0]=random.randint(0,750)
            enemypos3[1]=0
            bulposx=-100
            bulposy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)
        if bulhit(bul2posx,bul2posy,enemypos3):
            enemypos3[0]=random.randint(0,750)
            enemypos3[1]=0
            bul2posx=-100
            bul2posy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)


            
        if enemypos4[1]<600:
            enemypos4[1]+=4
        else:
            enemypos4[0]=random.randint(0,750)
            enemypos4[1]=0
        if collision(controller,enemypos4):
            out=font2.render('GAME OVER!',1,RED)
            screen.blit(out,(170,250))
            pygame.display.update()
            winsound.PlaySound(outt,winsound.SND_ASYNC)
            gameover=True
        if bulhit(bulposx,bulposy,enemypos4):
            enemypos4[0]=random.randint(0,750)
            enemypos4[1]=0
            bulposx=-100
            bulposy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)
        if bulhit(bul2posx,bul2posy,enemypos4):
            enemypos4[0]=random.randint(0,750)
            enemypos4[1]=0
            bul2posx=-100
            bul2posy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)

            
        if enemypos5[1]<600:
            enemypos5[1]+=5
        else:
            enemypos5[0]=random.randint(0,750)
            enemypos5[1]=-3000
        if collision(controller,enemypos5):
            enemypos1[0]=random.randint(0,750)
            enemypos1[1]=-1000
            enemypos2[0]=random.randint(0,750)
            enemypos2[1]=-1000
            enemypos3[0]=random.randint(0,750)
            enemypos3[1]=-1000
            enemypos4[0]=random.randint(0,750)
            enemypos4[1]=-1000
            enemypos7[0]=random.randint(0,750)
            enemypos7[1]=-1000
            enemypos5[0]=random.randint(0,750)
            enemypos5[1]=-1000
            winsound.PlaySound(woosh,winsound.SND_ASYNC)

            
        if enemypos7[1]<600:
            enemypos7[1]+=9
        else:
            enemypos7[0]=random.randint(0,750)
            enemypos7[1]=0
        if collision(controller,enemypos7):
            out=font2.render('GAME OVER!',1,RED)
            screen.blit(out,(170,250))
            pygame.display.update()
            winsound.PlaySound(outt,winsound.SND_ASYNC)
            gameover=True
        if bulhit(bulposx,bulposy,enemypos7):
            enemypos7[0]=random.randint(0,750)
            enemypos7[1]=0
            bulposx=-100
            bulposy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)
        if bulhit(bul2posx,bul2posy,enemypos7):
            enemypos7[0]=random.randint(0,750)
            enemypos7[1]=0
            bul2posx=-100
            bul2posy=-100
            winsound.PlaySound(punch,winsound.SND_ASYNC)
            
        #BACKGROUND MOVEMENT
            
        bgy+=3
        if bgy==0:
            bgy=-3000
            
        #bullet movement
            
        if bulposx<800 and bulposx>0:
            if bulposy>0 and bulposy<600:
                bulposy-=5
                screen.blit(bullet,(bulposx,bulposy))

        if bul2posx<800 and bul2posx>0:
            if bul2posy>0 and bul2posy<600:
                bul2posy-=5
                screen.blit(bullet,(bul2posx,bul2posy))

        #BOSS ALIEN
                
        health=font3.render("BOSS:"+hlt,1,RED)
        
        if score >= 2000 and balive:
            pygame.draw.rect(screen,RED,(bos1posx,bos1posy,150,75))
            screen.blit(boss1,(bos1posx,bos1posy))
            if bos1posx>=0 and bos1posx<=650:
               if bos1posx==0:
                   touch+=1
               if touch==1:
                   bos1posx+=2
               if bos1posx==650:
                   touch-=1
               if touch==0:
                   bos1posx-=2
                   
        if bosshit(bos1posx,bos1posy,bulposx,bulposy):
            damage-=1
            hlt=(damage//3)*"|"
            health=font3.render("BOSS:"+hlt,1,RED)
            if damage<=0:
                bos1posx=801
                balive=False

        if balive and score > 2000:
            screen.blit(health,(600,100))
                          
        if bosshit(bos1posx,bos1posy,bul2posx,bul2posy):
            damage-=1
            hlt=(damage//3)*"|"
            health=font3.render("BOSS:"+hlt,1,RED)
            if damage<=0:
                bos1posx=801
                balive=False
                   
        #ASTEROID CREATION
                
        pygame.draw.rect(screen,BLUE,(controller[0],controller[1],control_size,control_size))
        screen.blit(spaceship,(controller[0],controller[1]))
    
        pygame.draw.rect(screen,RED,(enemypos1[0],enemypos1[1],50,50))
        screen.blit(obstacle,(enemypos1[0],enemypos1[1]))
    
        pygame.draw.rect(screen,RED,(enemypos2[0],enemypos2[1],50,50))
        screen.blit(obstacle,(enemypos2[0],enemypos2[1]))
    
        pygame.draw.rect(screen,RED,(enemypos3[0],enemypos3[1],50,50))
        screen.blit(obstacle,(enemypos3[0],enemypos3[1]))

        pygame.draw.rect(screen,RED,(enemypos4[0],enemypos4[1],50,50))
        screen.blit(obstacle,(enemypos4[0],enemypos4[1]))
    
        pygame.draw.rect(screen,RED,(enemypos7[0],enemypos7[1],50,50))
        screen.blit(obstacle,(enemypos7[0],enemypos7[1]))
    
        pygame.draw.rect(screen,GREEN,(enemypos5[0],enemypos5[1],50,50))
        screen.blit(bomb,(enemypos5[0],enemypos5[1]))

        #SCORE TK
        
        lab2=Label(frame,font=('Helvetica','20'),fg="green",text="SCORE:"+str((score//2)//10))
        lab2.place(relx=0.1,rely=0.55,relheight=0.1,relwidth=0.3)
        
        #SCORE DISPLAY
        
        score+=1
        Score=font1.render('Score: '+str((score//2)//10),1,RED)
        screen.blit(Score,(650,550))
        pygame.display.update()

        clock.tick(tim)
        pygame.display.update()

        if gameover==True:
            pygame.mixer.music.stop()

        ############################################################ FILE WRITING #####################################################
        
    f=open('score.txt','a')
    f.write(name+(20-len(name))*" "+str((score//2)//10))
    f.write('\n')
    f.close()
    
        
###################################################################### TKINTER STARTING PAGE #################################################################
    
def star(x,y):
    lab3=Label(frame)
    lab3.place(relx=x,rely=y,relheight=0.002,relwidth=0.002)
    
root.iconbitmap(icon)

canvas=Canvas(root,height=800,width=1000,bg="green")
canvas.pack()

frame=Frame(root,bg="black")
frame.place(relheight=0.9,relwidth=0.9,relx=0.054,rely=0.055)

for i in range(500):
    star(random.random(),random.random())

def instruction():
    lab2=Label(frame,font=('Helvetica', '20'),text="""     HOW TO PLAY
    Help the alien dodge the Asteroids.
    Use the arrow keys to move
    up,down,right or left.Get
    the special bomb to destroy
    all the asteroids on screen.
    Hit spacebar to shoot bullets.
    Longer you survive,bigger
    your score.""",bg="black",fg="green")
    lab2.place(relx=0.4,rely=0.25,relheight=0.4,relwidth=0.6)

def difficulty():
    button4=Button(frame,text="EASY",fg="green",font=('Helvetica','20'),command=easy)
    button4.place(relx=0.44,rely=0.7,relwidth=0.15,relheight=0.1)

    button5=Button(frame,text="MEDIUM",fg="green",font=('Helvetica','20'),command=medium)
    button5.place(relx=0.64,rely=0.7,relwidth=0.15,relheight=0.1)

    button6=Button(frame,text="HARD",fg="green",font=('Helvetica','20'),command=hard)
    button6.place(relx=0.84,rely=0.7,relwidth=0.15,relheight=0.1)
    
def easy():
    global tim
    tim=90
    lab8=Label(frame,text="^",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.5,rely=0.8,relheight=0.04,relwidth=0.04)

    lab8=Label(frame,text="",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.7,rely=0.8,relheight=0.04,relwidth=0.04)

    lab8=Label(frame,text="",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.9,rely=0.8,relheight=0.04,relwidth=0.04)

def medium():
    global tim
    tim=120
    lab8=Label(frame,text="^",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.7,rely=0.8,relheight=0.04,relwidth=0.04)

    lab8=Label(frame,text="",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.5,rely=0.8,relheight=0.04,relwidth=0.04)

    lab8=Label(frame,text="",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.9,rely=0.8,relheight=0.04,relwidth=0.04)

def hard():
    global tim
    tim=140
    lab8=Label(frame,text="^",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.9,rely=0.8,relheight=0.04,relwidth=0.04)

    lab8=Label(frame,text="",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.5,rely=0.8,relheight=0.04,relwidth=0.04)

    lab8=Label(frame,text="",font=('Helvetica','30'),fg="green",bg="black")
    lab8.place(relx=0.7,rely=0.8,relheight=0.04,relwidth=0.04)
    
########################################################################## NAME INPUT ########################################################################

name=input('ENTER YOUR NAME:')
score=0

button1=Button(frame,font=('Helvetica', '20'),text="START",fg="green",command=startgame)
button1.place(relheight=0.1,relwidth=0.3,relx=0.1,rely=0.25)

lab1=Label(frame,font=('Helvetica', '40'),text="ASTEROIDS 2.0",fg="green",bg="white")
lab1.place(relx=0.1,rely=0.0,relheight=0.2,relwidth=0.8)

button2=Button(frame,font=('Helvetica', '20'),text="INSTRUCTION",fg="green",command=instruction)
button2.place(relx=0.1,rely=0.4,relheight=0.1,relwidth=0.3)

lab2=Label(frame,font=('Helvetica', '20'),fg="green",text="SCORE:0")
lab2.place(relx=0.1,rely=0.55,relheight=0.1,relwidth=0.3)

button3=Button(frame,text="DIFFICULTY",font=('Helvetica','20'),fg="green",command=difficulty)
button3.place(relx=0.1,rely=0.7,relwidth=0.3,relheight=0.1)

photo=PhotoImage(file=whiteasteroid)
lab9=Label(frame,image=photo,bg='white')
lab9.place(relx=0.12,rely=0.02,relwidth=0.15,relheight=0.15)

lab10=Label(frame,image=photo,bg='white')
lab10.place(relx=0.74,rely=0.02,relwidth=0.15,relheight=0.15)

lab11=Label(frame,text='Copyright 2019 - 2020, Maze Games, Inc. All rights reserved',bg='black',fg='white',font=('Helvetica','15'))
lab11.place(relx=-0.015,rely=0.95,relwidth=0.8,relheight=0.04)

######################################################################### FILE READING #######################################################################

f1=open('score.txt','r')
hscore='0'
try:
    for i in f1:
        l=i.split()
        if int(l[1])>int(hscore):
            hscore=l[1]
except IndexError:
    pass
f1.close()

lab7=Label(frame,font=('Helvetica', '20'),fg="green",text="HIGHEST SCORE:"+hscore)
lab7.place(relx=0.3,rely=0.85,relheight=0.1,relwidth=0.4)

























