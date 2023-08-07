import random 
#  FUNCTION CODE :
def DiceSimulator(m,Players):
    x = "y"
    player_no=1  #starting from player 1.
    while x == "y":
        no = random.randint(1,6)  #to generate random number between 1 to 6 including them.
        if m==2:     
            if player_no > Players:
                player_no=1
            print("Player {}".format(player_no))  #to print current player

        if no == 1:
            print("[-------]")
            print("[       ]")
            print("[   0   ]")
            print("[       ]")
            print("[-------]")
        if no == 2:
            print("[-------]")
            print("[  0    ]")
            print("[       ]")
            print("[    0  ]")
            print("[-------]")
        if no == 3:
            print("[-------]")
            print("[ 0     ]")
            print("[   0   ]")
            print("[     0 ]")
            print("[-------]")
        if no == 4:
            print("[-------]")
            print("[ 0   0 ]")
            print("[       ]")
            print("[ 0   0 ]")
            print("[-------]")
        if no == 5:
            print("[-------]")
            print("[ 0   0 ]")
            print("[   0   ]")
            print("[ 0   0 ]")
            print("[-------]")
        if no == 6:
            print("[-------]")
            print("[ 0   0 ]")
            print("[ 0   0 ]")
            print("[ 0   0 ]")
            print("[-------]")
            print("\n")
            if m==1 :
                print("Yeah!! You got extra chance ,Roll Again !")
            if m==2 :
                #to know which player got an extra chance
                print("Yeah!! Player {}, got extra chance ,Roll Again !".format(player_no))  
                player_no-=1 # To give same player the extra chance.
    
        player_no+=1 #each time player should be incremented to give next player a chance.
        if m==2:
            if player_no>Players:   
                player_no=1     #to start next set of chances from Player 1
            print("Next : Player {}".format(player_no))   #to print next player
        
        x=input("\t\nPress y to roll and n to exit:")
        print("\n")
 
    
#  DRIVER CODE :
print ('***** WELCOME TO DICE ROLLING SIMULATOR *****')

players=int(input("\t\nEnter the number of Players :"))

while (players<=0):
    print("Oops!! Insufficient Players !")
    players=int(input("\t\nEnter the number of Players :"))
    
if (players==1):     
        DiceSimulator(1,players)           #function call for single player.
else :
        DiceSimulator(2,players)         #function call for multi-player.
        
        








