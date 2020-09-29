
import random
import time

money = 10

print(f"Welcome to Profit Simulator: Millenium Edition!")

def main():
	print("Please enter of the following options.")
	print("1. Donate\n" + "2. Burn\n" + "3. Stonks\n" + "4. Gamble\n")
	spend = input(f"You have ${format(money, '.2f')}. What would you like to do?\n")
	if spend == "1":
		donate()
	elif spend == "2":
		burn()
	elif spend == "3":
		stonks()
	elif spend == "4":
		gamble()
				
def donate():
	global money
	amount = float(input("How much would you like to donate?\n"))
	if amount > money:
		print(f"You do not have that much money. You only have ${format(money, '.2f')}.")
	else:
		# Deduct money
		money -= amount
		print(f"Transaction completed successfully! You have donated ${format(amount, '.2f')}.")
	
def burn():
	global money
	amount = float(input("How much would you like to burn?\n"))
	if amount > money:
		print(f"You do not have that much money. You only have ${format(money, '.2f')}.")
	else:
		# Deduct money
		money -= amount
		print(f"You have burned ${format(amount, '.2f')}.")

def stonks():
	global money
	amount = float(input("How much would you like to invest?\n"))
	if amount > money:
		print(f"You do not have that much money. You only have ${str(money)}.")
	else:
		print(f"Investing ${format(amount, '.2f')} for 5 seconds.")
		for i in range(0, 4):
			time.sleep(1)
			print(".", end="")
		change = amount * (random.randrange(-5, 30)/100)
		money += change
		if change > 0:
			print(f"You made ${format(change, '.2f')}!")
		elif change < 0:
			print(f"You lost ${format(0-change, '.2f')}.")
		else:
			print("Your money did not change.")

def gamble():
	global money
	amount = float(input("How much would you like to gamble?\n"))
	if amount > money:
		print(f"You do not have that much money. You only have ${str(money)}.")
	else:
		print(f"Gambling ${format(amount, '.2f')}...")
		change = amount * (random.randrange(-100, 100)/100)
		money += change
		if change > 0:
			print(f"You made ${format(change, '.2f')}!")
		elif change < 0:
			print(f"You lost ${format(0-change, '.2f')}.")
		else:
			print("Your money did not change.")

while(True):
	main()
	if money == 0:
		print("You've lost bud")
		break
