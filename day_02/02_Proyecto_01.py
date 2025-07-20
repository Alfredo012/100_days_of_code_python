print("Welcome to the tip calculator")
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
total = (float(bill) * (((float(tip)/100)) + 1))/ float(people)
print("Each person should pay: " + str(round(total, 2)))


