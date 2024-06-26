#Rock-Paper-Scissors Game
'''
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
Display Result: Show the user's choice and the computer's choice.
Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
Play Again: Ask the user if they want to play another round.
'''
import random
l=['Stone', 'Paper', 'Scissors']
def play(u):
    c=l[random.randint(0,2)]
    print("Computer's Choice: ",c)
    if(c=='Stone'):
        if u=='Stone':
            print('Tie')
        elif u=='Paper':
            print('You lost')
        elif u=='Scissors':
            print('You won')
        else:
            print("Error... Try again")
        
    elif(c=='Paper'):
        if u=='Stone':
            print('You won')
        elif u=='Paper':
            print('Tie')
        elif u=='Scissors':
            print('You lost')
        else:
            print("Error... Try again")
    else:
        if u=='Stone':
            print('You lost')
        elif u=='Paper':
            print('You won')
        elif u=='Scissors':
            print('Tie')
        else:
            print("Error... Try again")
            
print("PLAY Stone, Paper Scissors!")
w='P'
while w=='P':
    u=input("Enter your choice... ")
    play(u)
    w=input("Press 'P' to play Again ").upper()
else:
    print("Thanks for Playing :)")
