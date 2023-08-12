
print("Welcome to the tip calculator.")
bill = int(input("What was the total bill? Rs : "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? : "))
people = int(input("How many people to split the bill? : "))
bill_with_tip = tip / 100 * bill + bill
print("Your total bill is : " + bill_with_tip)
