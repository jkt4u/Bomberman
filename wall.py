

class Wall():											

    def __init__(self,Matrix):									#initialises object of class wall				
        
        for x in range(40):
            for y in range(84):
                if x<=1 or x>=38 or y<=3 or y>=80:				#print '#' at required places
                    Matrix[x][y]='#'

        for x in range(2,38):
            for y in range(4,80):
                if (x%4==0 or (x-1)%4==0) and (y%8==0 or (y-1)%8==0 or (y-2)%8==0 or (y-3)%8==0):
                    Matrix[x][y]='#'							#print '#' at required places				
