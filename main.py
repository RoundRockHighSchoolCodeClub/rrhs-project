# Code here!
money = 10

print(f"Welcome to Profit Simulator: Millenium Edition!")

def main():
	print("1. Donate\n" + "2. Burn\n")
	spend = input(f"You have ${str(money)}. How would you like to spend it?\n")
	if spend == "1":
		donate()
	elif spend == "2":
		burn()
				
def donate():
	amount = int(input("How much would you like to donate?\n"))
	if amount > money:
		print(f"You do not have that much money. You only have ${str(money)}.")
	else:
		# Deduct money
		money -= amount
		print(f"Transaction completed successfully! You have donated ${str(amount)}.")
	
def burn():
	amount = int(input("How much would you like to burn?\n"))
	if amount > money:
		print(f"You do not have that much money. You only have ${str(money)}.")
	else:
		# Deduct money
		money -= amount
		print(f"You have burned ${str(amount)}.")

while(True):
	main()
	if money == 0:
		print("You've lost bud")
		break
