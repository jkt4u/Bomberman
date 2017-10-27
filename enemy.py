import random
import time
class enemy:
    def __init__(self,Matrix):                                    #initialises object of class enemy
        x=random.randint(4,39)
        while x%2!=0:
            x=random.randint(4,39)
    
        y=random.randint(4,76)                                    #find random x and y coordinates for enemy      
        while y%4!=0:
            y=random.randint(4,76)
            
        while(Matrix[x][y]=='#' or Matrix[x][y]=='/'):            # checking if brick or not
            x=random.randint(4,39)
            while x%2!=0:
                x=random.randint(4,39)
    
            y=random.randint(4,76)
            while y%4!=0:
                y=random.randint(4,76)
        
        self.x=x
        self.y=y
        for k in range(4):
            Matrix[x][y]="E"                                       #print 8 E      
            Matrix[x+1][y]="E"
        
            y+=1

    def move(self,Matrix):                                         #define move function for enemy 
        x1=self.x
        y1=self.y
        rand=random.randint(1,4)                                   #select random number from 1 to 4 
        if rand ==1:
            x1=self.x
            y1=self.y
            if Matrix[self.x-1][self.y]!='#' and Matrix[self.x-1][self.y]!='/' and Matrix[self.x-1][self.y]!='B' and Matrix[self.x-1][self.y]!='E':
                for k in range(4):
                    Matrix[self.x][self.y]=" "
                    Matrix[self.x+1][self.y]=" "
                    self.y+=1                                       
                self.x-=2
                self.y=y1
                for k in range(4):
                    Matrix[self.x][self.y]="E"
                    Matrix[self.x+1][self.y]="E"
                    self.y+=1
                self.y=y1
        
        elif rand==2:                                              #if random no is 2 enemy moves to left
            if Matrix[self.x][self.y-1]!='#' and Matrix[self.x][self.y-1]!='/' and Matrix[self.x][self.y-1]!='B' and Matrix[self.x][self.y-1]!='E':
                for k in range(4):
                    Matrix[self.x][self.y]=" "
                    Matrix[self.x+1][self.y]=" "
                    self.y+=1
                self.x=x1
                self.y=y1-4
                for k in range(4):
                    Matrix[self.x][self.y]="E"
                    Matrix[self.x+1][self.y]="E"
                    self.y+=1
                self.y=y1-4
        
        elif rand==3:                                               #if random no is 3 enemy moves to right
            if Matrix[self.x][self.y+4]!='#' and Matrix[self.x][self.y+4]!='/' and Matrix[self.x][self.y+4]!='B' and Matrix[self.x][self.y+4]!='E':
                for k in range(4):
                    Matrix[self.x][self.y]=" "
                    Matrix[self.x+1][self.y]=" "
                    self.y+=1
                self.x=x1
                self.y=y1+4
                for k in range(4):
                    Matrix[self.x][self.y]="E"
                    Matrix[self.x+1][self.y]="E"
                    self.y+=1
                self.y=y1+4

        elif rand==4:                                                 #if random no is r enemy moves backward
            if Matrix[self.x+2][self.y]!='#' and Matrix[self.x+2][self.y]!='/' and Matrix[self.x+2][self.y]!='B' and Matrix[self.x+2][self.y]!='E':
                for k in range(4):
                    Matrix[self.x][self.y]=" "
                    Matrix[self.x+1][self.y]=" "
                    self.y+=1
                self.x+=2
                self.y=y1
                for k in range(4):
                    Matrix[self.x][self.y]="E"
                    Matrix[self.x+1][self.y]="E"
                    self.y+=1
                self.y=y1

    def kill(self,ene,k):                                       # kill function to remove enemy from ene array
        ene.pop(k)  

        

