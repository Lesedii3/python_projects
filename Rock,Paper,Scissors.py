import random

print("=== Rock,Paper,Scissors === ")
comp_choice=random.randint(0,2)
user_choice= int(input("Type 0 for rock,1 for paper and 2 for scissors: "))

if user_choice ==0:
    print("You chose rock.")
elif user_choice==1:
    print("You choose paper.")
elif user_choice==2:
    print("You chose scissors.")
else:
    print("Invalid input")
    exit()

if comp_choice==0:
    print("Computer chose rock.")
elif comp_choice==1:
    print("Computer chose paper.")
elif comp_choice==2:
    print("Computer chose scissors.")

if user_choice==comp_choice:
    print("Its draw.")
elif user_choice ==0 and comp_choice==1:
    print("Computer wins,you lose :( ")
elif user_choice==0 and comp_choice==2:
    print("You win :),Computer loses.")





