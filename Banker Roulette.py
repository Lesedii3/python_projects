
import random
print("====== Welcome to the Banker Roulette ======")
print("Wondering who is going to pay for the bill today, let's find out!!")
names = input("Enter the names of your friends, separated by commas: ")

# Split the input string into a list of names
umn = names.split(", ")

# Check if the list is not empty
if umn:
    person = random.choice(umn)
    print(f"{person} is going to pay for the bill!")
else:
    print("No names were entered.")
