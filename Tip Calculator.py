print("Hello There,Welcome to the tip calculator!")
bill=float(input("What was your total bill?"))
people=int(input("How many people would you like to split it with?"))
tip=int(input("How much percentage would you like to tip: 10,12,15%?"))

tip_as_percentage= tip/100
billd= bill*tip_as_percentage
total= (billd+bill)/people
totally = round(total,2)
print(f"Each individual has to pay R{totally}")