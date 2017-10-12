import time
import config
def print_Matrix(mat):
	for _ in mat:
		print("".join(_))

class bomb:
	def __init__(self,x1,y1,Matrix):                   #initialises object of class bomb
		self.x=x1
		self.y=y1
		x2=x1                                          #coordinates of bomb are stored
		y2=y1
		
		for k in range(4):
			Matrix[x2][y2]="e"						   #8 e are printed 
			Matrix[x2+1][y2]="e"
			y2+=1
		self.x=x1
		self.y=y1
		
	def detonate(self,Matrix,B,ene):				   #Function to detonate the bomb
		flag=0
		x2=self.x
		y2=self.y
		x3=x2
		y3=y2
		x4=x3
		x5=x3
		y4=y3
		y5=y4
		x6=x5
		y6=y5
		
		
		if Matrix[x2][y2-4]!="#" and Matrix[x2][y2+4]!="#" :
			if Matrix[x4][y4-1]=='E':                       
					flag=1											#if enemy is found on detonation path flag is set to 1 and coordinates are stored
					c1=x4
					c2=y4-4
					

			if Matrix[x4][y4+5]=='E':                   
					flag=1
					c1=x4
					c2=y4+4
					
			if Matrix[x4][y4]=='E':
					flag=1
					c1=x4
					c2=y4+4
					                     
			if Matrix[x4][y4-1]=='/':
					config.score+=20
					
			if Matrix[x4][y4+5]=='/':
					config.score+=20					
			if Matrix[x4][y4]=='/':
					config.score+=20	

			if Matrix[x4][y4-1]=='B' or Matrix[x4][y4+5]=='B' or Matrix[x4][y4]=='B':
					B.x=2
					B.y=4
					config.lives-=1
				
				
			for k in range(12):
				
						 
				

				Matrix[x2][y2-4]="*"							#  * is printed after detonation
				Matrix[x2+1][y2-4]="*"
				y2+=1

		

		else:
			for j in range(4):
				Matrix[x2][y2]=" "
				Matrix[x2+1][y2]=" "
				y2+=1

		if flag==1:												#if enemy was in the path 
			config.score+=100									# find the corresponding enemy in ene array and kill it by calling ene[].kill()
			for r in range(len(ene)):
				

				if ene[r].x==c1 and ene[r].y==c2:
					ene[r].kill(ene,r)
					flag=0
					break

	   

		if Matrix[x3-1][y3]!="#" and Matrix[x3+2][y3]!="#" :
			
			if Matrix[x5-2][y5]=='E':
				flag=1
				c1=x5-2
				c2=y5

			if Matrix[x5][y5]=='E':
				flag=1
				c1=x5
				c2=y5
			if Matrix[x5+2][y5]=='E':
				flag=1
				c1=x5+2
				c2=y5

			if Matrix[x5-2][y5]=='/':
				config.score+=20
			if Matrix[x5][y5]=='/':
				config.score+=20
			if Matrix[x5+2][y5]=='/':
				config.score+=20


			if Matrix[x5-2][y5]=="B" or Matrix[x5][y5]=="B" or Matrix[x5+2][y5]=="B":
				B.x=2
				B.y=4
				config.lives-=1
				
			for k in range(4):
				
				 
				Matrix[x3-2][y3]="*"
				Matrix[x3-1][y3]='*' 
				
				Matrix[x3][y3]="*"
				Matrix[x3+1][y3]="*"
				Matrix[x3+2][y3]="*"
				Matrix[x3+3][y3]="*"
				y3+=1
		else:
			for j in range(4):
				Matrix[x6][y6]=" "
				Matrix[x6+1][y6]=" "
				y6+=1

		if flag==1:
			config.score+=100
					
			for k in range(len(ene)):
				if ene[k].x==c1 and ene[k].y==c2:
					ene[k].kill(ene,k)

					flag=0
					break



		print_Matrix(Matrix)									#prints matrix showing explostion
		time.sleep(2)											#pauses for 2 seconds
		x3=self.x
		y3=self.y
		x4=self.x
		y4=self.y
		if Matrix[x3][y3-4]!="#" and Matrix[x3][y3+4]!="#" :
		 
			for k in range(12):

	
				Matrix[x3][y3-4]=" "
				Matrix[x3+1][y3-4]=" "							#remove the * with empty spaces
				y3+=1
		y3=y3-4        
		if Matrix[x4-1][y4]!="#" and Matrix[x4+2][y4]!="#" :
			
			for k in range(4):
	
				Matrix[x4-2][y4]=" "
				Matrix[x4-1][y4]=' ' 
				
				Matrix[x4][y4]=" "
				Matrix[x4+1][y4]=" "
				Matrix[x4+2][y4]=" "
				Matrix[x4+3][y4]=" "
				y4+=1
		
		
			
		print_Matrix(Matrix)

	