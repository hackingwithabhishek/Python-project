# Rock paper scissors Game 
# Rock VS paper ==> paper wins
# rock vs scissors ==> rock wins
# paper VS scissors ==> scissors wins
# c=0
# for i in range(1,5):
#     c=c+1
#     print (c,i)
import random
list=["rock","scissors","paper"]


while(True):
    ucount=0
    Ccount=0
    userinput=int(input("""
        1- start game
        2-NO/exit game                   
        """))
    if userinput ==1:
        for i in range(1,6):
            user=int(input("""
            1>=Rock
            2>=paper
            3>=Scissors
            """))
            if  user==1:
                uchoice="rock" # user input choice
            elif user==2:
                uchoice="paper"
            elif user==3:
                uchoice="scissors"
            else:
                print("worng output")
            Comchoice=random.choice(list)# computer choice 
            if uchoice==Comchoice:
                print(" user input choice::--",uchoice)  
                print(" computer choice:--",Comchoice) 
                print("Game Draw")
                ucount=ucount+1 
                Ccount=Ccount+1 
            elif (uchoice=="paper" and Comchoice=="rock") or (uchoice=="Scissors" and 
                Comchoice=="paper") or (uchoice=="rock" and Comchoice=="scissors"):
                print(" user input choice::--",uchoice)  
                print(" computer choice:--",Comchoice) 
                print ("You Win The Game")
                ucount=ucount+1 
            else:
                print(" user input choice::--",uchoice)  
                print(" computer choice:--",Comchoice) 
                print("Computer are Win")
                Ccount=Ccount+1
        print(     )
        if ucount>Ccount:
            print ("Final Result:--")
            print("Total no. of your",ucount)
            print("Total no. of your",Ccount)
            print(" You are win this game")
        elif ucount<Ccount:
            print ("Final Result:--")
            print("Total no. of your",ucount)
            print("Total no. of your",Ccount)
            print ("Computer are Win ") 
        else :
            print("Final Result:--")
            print("Total no. of your",ucount)
            print("Total no. of your",Ccount)
            print("Game are Draw So Replay this game")        
    else:
        break
        