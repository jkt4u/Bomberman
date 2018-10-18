class bomberman:
    def __init__(self,Matrix):                              #initialises class bomberman
      
        
      self.x=2
      self.y=4
      x=2
      y=4
      for k in range(4):
          Matrix[x][y]="B"
          Matrix[x+1][y]="B"
        
          y+=1
        
    def move(self,key,Matrix):                              #initialises move function for bomberman                            
        x1=self.x
        y1=self.y
                
        



        if key=='q':
            exit(0)
        if key=='w':                                        #if w is presses bomberman moves forward after checking that free space is there
            if Matrix[self.x-1][self.y]!='#' and Matrix[self.x-1][self.y]!='/' and Matrix[self.x-1][self.y]!='E':
                if Matrix[self.x][self.y]!='e':
                    
                    for k in range(4):                      #Clear the old coordinates
                            Matrix[self.x][self.y]=" "
                            Matrix[self.x+1][self.y]=" "
                            self.y+=1
                self.x-=2
                self.y=y1
                for k in range(4):                          #Print 8 B at new coordinates
                    
                    Matrix[self.x][self.y]="B"
                    Matrix[self.x+1][self.y]="B"
                    self.y+=1
                self.y=y1
        elif key=='a':                                       #if a is pressed bomberman moves to left 
            if Matrix[self.x][self.y-1]!='#' and Matrix[self.x][self.y-1]!='/' and Matrix[self.x][self.y-1]!='E':
                if Matrix[self.x][self.y]!='e':
                
                    for k in range(4):                       #clear the old coordinates
                    
                        Matrix[self.x][self.y]=" "
                        Matrix[self.x+1][self.y]=" "
                        self.y+=1
                self.x=x1
                self.y=y1-4
                for k in range(4):                            #print 8 B at the new coordinates
                    Matrix[self.x][self.y]="B"
                    Matrix[self.x+1][self.y]="B"
                    self.y+=1
                self.y=y1-4
        elif key=='d':                                        #moves to the right
            if Matrix[self.x][self.y+4]!='#' and Matrix[self.x][self.y+4]!='/' and Matrix[self.x][self.y+4]!='E':
                if Matrix[self.x][self.y]!='e':
                
                    for k in range(4):                        #clears the old coordinates
                    
                        Matrix[self.x][self.y]=" "
                        Matrix[self.x+1][self.y]=" "
                        self.y+=1 
                self.x=x1
                self.y=y1+4
                for k in range(4):                            #print 8 B at new coordinates
                    Matrix[self.x][self.y]="B"
                    Matrix[self.x+1][self.y]="B"
                    self.y+=1
                self.y=y1+4

        elif key=='s':                                        #moves backward
            if Matrix[self.x+2][self.y]!='#' and Matrix[self.x+2][self.y]!='/' and Matrix[self.x+2][self.y]!='E':
                if Matrix[self.x][self.y]!='e':
                
                    for k in range(4):                        #clears the old coordinates
                    
                        Matrix[self.x][self.y]=" "
                        Matrix[self.x+1][self.y]=" "
                        self.y+=1
                self.x+=2
                self.y=y1
                for k in range(4):                            #print 8 B at new coordinates
                    Matrix[self.x][self.y]="B"
                    Matrix[self.x+1][self.y]="B"
                    self.y+=1
                self.y=y1
