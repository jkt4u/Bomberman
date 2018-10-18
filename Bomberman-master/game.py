import random
import os
import signal
import config
from wall import *
from brick import *
from bomberman import *
from enemy import *
from bomb import *
import time

 
bom=0
config.lives=3                                         #lives is global variable denoting lives left
config.score=0                                         #Score is global variable denoting player's score 
w=84
h=40
Matrix=[[' ' for a in range(w)] for b in range(h)]     #Creates a matrix with width w=84 and height h=40

class GetchUnix:                                       #It is used to take input from user
    def __init__(self):
        import tty 

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
getch = GetchUnix()

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    
    try:
        text = getch()
        signal.alarm(0)
        
        return text
    except AlarmException:
        
        for k in range(len(ene)):
            ene[k].move(Matrix)
        
        

    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''






def print_Matrix(mat):                                #Function to print matrix                          
    for _ in mat:
        print("".join(_))
     
w=84
h=40

x=Wall(Matrix)                                        #Creates an object of class wall


for k in range(20):
    Brick1=brick(Matrix)                              #Creates objects of class brick      




        
B=bomberman(Matrix)                                   #Creates object of class bomberman
ene=[]                                                #Creates object of enemy class and add it in ene array
for i in range(4):
    ene.append(enemy(Matrix))



print_Matrix(Matrix)

count=-1
while(True):                                          #Start an infinte loop taking inputs
    key=input_to()                                    #Take input from user
    if key=='b' and count==-1:
        count=5
        
        # print('dsd')
        bo=bomb(B.x,B.y,Matrix)                       #Creates object of class bomb which is created after pressing b
    if count>0:
        count-=1
    if count==0 :
        count-=1
        bo.detonate(Matrix,B,ene)                     #function is called to detonate the bomb after count becomes 0
        
    B.move(key,Matrix)                                #Call the function B.move that moves our bomberman and give key as its parameter
    for k in range(len(ene)):                         #Call the function ene[k].move to move the enemy
        ene[k].move(Matrix)
    
    os.system('clear')                                #clears the terminal screen 
    #print(ene)
    if config.lives==0:
        exit(0  )
    print_Matrix(Matrix)                              #prints the matrix
    print('\n')
    print("Lives : " + str(config.lives) + " Score : " + str(config.score))   #prints lives and score
