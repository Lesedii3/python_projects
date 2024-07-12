
print("Welcome to the ultimate LOVE CALCULATOR")
name1=input("Enter the name of your lover or crush :")
name2=input("Enter your name :")
print("The love calculator is calculating your score...")
#combining the words together
cold=name1+name2
combined=cold.lower()
#Calculating the occurance of each letter in the word
t=combined.count("t")
r=combined.count("r")
u=combined.count("u")
e=combined.count("e")
#Calculating the occurance of each letter in the word
l=combined.count("l")
o=combined.count("o")
v=combined.count("v")
e=combined.count("e")
#Adding them together
first_num=t+r+u+e
sec_digit=l+o+v+e

anew= str(first_num)+str(sec_digit)
new=int(anew)

if new>50 and new<60:
    print(f"Your score is {new},you are good for each other \n JUST FOR THE SAKE OF MJOLO EN STUFF.")
elif new<50 :
    print(f"Your score is {new},you guyzz are not really meant for each other\n SORRY :( ")
else:
    print(f"Your score is {new},you guyz are meant for each other \n ITS GIVING WEDDING BELLSSS.")

