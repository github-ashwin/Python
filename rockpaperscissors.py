import random

options = ('rock','paper','scissors') #Tuple storing constants
play=True
while play:
    user=None
    computer = random.choice(options) #Choosing random form tuple
    while user not in options:
        user = input("Enter a choice (rock, paper, scissors): ") #User inputs their choice

#Display of choices
    print("User: ",user)
    print("Computer: ",computer)
    
    #Conditions
    if(user==computer):
        print("It's a tie!")
    elif(user=='rock' and computer=='paper'):
        print("Computer wins")
    elif(user=='paper' and computer=='rock'):
        print("User wins")
    elif(user=='rock' and computer=='scissors'):
        print("User wins")
    elif(user=='scissors' and computer=='rock'):
        print("Computer wins")
    elif(user=='paper' and computer=='scissors'):
        print("Computer wins")
    elif(user=='scissors' and computer=='paper'):
        print("User wins")
    else:
        print("Wrong choice")
    
    retry=input("Try Again (y/n): \n") #Try again condition
    if(retry!='y'):
        play=False