import random

# game essentials
options=["rock","paper","scissor"]
game_no=1 
user_score=0
ai_score=0

# scorecard//start of the game
def Scorecard():
    print(f"""GAME NUMBER {game_no}        YOUR SCORE:{user_score}          AI SCORE:{ai_score}""")
    return input("enter your choice (rock\U0001FAA8  , paper\U0001F4C4 , scissor\u2702  ) or exit: ").lower()


while True:
            userChoice=Scorecard() 
            #ending scorecard
            if(userChoice == "exit"):
                print("\n*********** GAME OVER ***********")
                
                print(f"\n You have played \"{game_no}\" gmaes out of which you won \"{user_score}\" and ai won \"{ai_score}\"  \n")
                if(user_score > ai_score):
                    print(f"YOU HAVE WON THE GAME WITH \"{user_score}\" GAME POINTS")
                elif(user_score < ai_score):
                    print(f"AI HAS WON THE GAME WITH \"{ai_score}\" GAME POINTS")
                else:
                    print(f"ITS A DRAW WITH EACH HAVING \"{user_score}\" GAME POINTS") 
                break    
            
            if userChoice not in options:
                print("\n\nInvalid input! Please choose rock, paper, or scissor.\n\n")
                continue
            
            
            randomChoice=random.choice(options)
            print(f"you have chosen {userChoice} and AI has chosen {randomChoice} ")  
            if(userChoice==randomChoice):
                print("its a draw \n" + "\n"+ "*"*30 +"\n")
            elif((userChoice=="paper" and randomChoice=="rock") or 
                (userChoice=="rock" and randomChoice=="scissor") or 
                (userChoice=="scissor" and randomChoice=="paper")):  
                print("you have won\n" +"\n"+ "*"*30 +"\n")
                user_score+=1
            else:
                print("better luck next time\n" + "\n"+ "*"*30 +"\n")
                ai_score+=1 
            game_no+=1              

      

    