#import pygame
#pygame.init()
def main():

#win = pygame.display.set_mode((500, 500))
  #pygame.display.set_caption("Extes 1")

 coords = ['1,1', '1,2', '1,3', '1,4', '1,5', '2,1', '2,2', '2,3', 
	'2,4', '2,5', '3,1', '3,2', '3,3', '3,4', '3,5', '4,1', '4,2', 
	'4,3', '4,4,', '4,5', '5,1','5,2', '5,3', '5,4', '5,5']
	
 mapp = ("* * * * *\n* - - - *\n* - * - *\n* O * * *\n* * * * *\n")
 # mapp = ("*****','*---*', '*-*-*', '*O***', '*****\n")
 print mapp 
 print ("You can move up, down, left or right, but if you try and move into a wall, you will die. Reach the end to win. Good luck!\n")
 prompt = raw_input("Move: ")
 location = coords[8]
	
	 #loop 
	  #  display map
	   # prompt
	    #check at coord that we want to move to if up testy = y -1, testx = x
	    #if cell is * 
	     #   say ouch you walked into a wall 
        #else if cell is '-'
         #   set new coords to be the checked coord	 x = testx and y = testy
    
 won = 0
 while won == 0:
	if prompt == "left" and location == '2,4' or location == '2,3' or location == '2,2' or location == '4,3':
		  print ("You are dead. Game over!")
	elif location == '3,2':
		  location = coords[11]
		  mapp =("* * * * *\n* O - - *\n* - * - *\n* - * * *\n* * * * *\n")
		  prompt = raw_input("Move: ")
		  print mapp
		  print location 
	elif location == '4,2':
		   location = coords[16]
		   mapp = ("* * * * *\n* - O - *\n* - * - *\n* - * * *\n* * * * *\n")
		   print mapp
		   print location
		   prompt = raw_input("Move: ")
		   
	if prompt == "right" and location == '2,4' or location == '2,3' or location == '4,5' or location == '4,3':
		 print ("You are dead. Game over!")
	elif location == '2,2':
		  location = coords[16]
		  mapp = ("* * * * *\n* - O - *\n* - * - *\n* - * * *\n* * * * *\n")
		  print mapp
		  print location
		  prompt = raw_input("Move: ")
	elif location == '3,2':
		  location = coords[21]
		  mapp = ("* * * * *\n* - - O *\n* - * - *\n* - * * *\n* * * * *\n")
		  print mapp
		  print location
		  prompt = raw_input("Move: ")
		  
	if prompt == "up" and location == '2,2' or location == '3,2' or location == '4,2':
		 print ("You are dead. Game over!")
	elif location == '2,4': 
		  mapp = ("* * * * *\n* - - - *\n* O * - *\n* - * * *\n* * * * *\n")
		  print mapp
		  print location
		  prompt = raw_input("Move: ")
	elif location == '2,3': 
		  mapp = ("* * * * *\n* O - - *\n* - * - *\n* - * * *\n* * * * *\n")
		  print mapp
		  print location
		  prompt = raw_input("Move: ")
		  
	if prompt == "down" and location == '2,4' or location == '3,2':
			print ("You are dead. Game over!")
	elif location == '2,3':
			location = '2,4'
			print mapp
			print location
			prompt = raw_input("Move: ")
	elif location == '2,2':
			location = '2,3'
			mapp = ("* * * * *\n* - - - *\n* O * - *\n* - * * *\n* * * * *\n")
			print mapp
			print location
			prompt = raw_input("Move: ")
	elif location == '4,2':
			location = '4,3'
			mapp = ("* * * * *\n* - - - *\n* - * O *\n* - * * *\n* * * * *\n")
			print mapp
			print location
			print("You got to the end: you win!")
		
	restart=raw_input("Start again?")
	if restart == "yes":
		main()
	else:
		exit()
main()
		
	
