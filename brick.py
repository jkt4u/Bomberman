import random
# bhen ka loda
class brick():                                                  
    def __init__(self,Matrix):                              #initialises object of class wall
        for k in range(10):
            x=random.randint(2,37)
            while x%2!=0:                                   #select x coordinate
                x=random.randint(2,37)
        

            y=[5,13,21,29,37,45,53,61,69,77]
            z=random.sample(set(y),1)                       #select y coordinate
            z=z[0]
          
        
        for y in range(4):                                  #print 8 /
            Matrix[x][z-1]="/"
            Matrix[x+1][z-1]="/"
            
            z+=1
