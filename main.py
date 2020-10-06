import random
options = ['rock','paper','scissors']
computer_option = random.choice(options)
player_option = None
while player_option not in options:
  player_option = input("Choose either rock, paper, or scissors: ")
if player_option == computer_option:
  print("Tie!")
  print(f"Computer chose {computer_option}")
elif player_option == 'rock' and computer_option == 'paper':
  print("Computer wins!")
  print(f"Computer chose {computer_option}")
elif player_option == 'paper' and computer_option == 'rock':
  print("You win!")
  print(f"Computer chose {computer_option}")
elif player_option == 'paper' and computer_option == 'scissors':
  print("You win!")
  print(f"Computer chose {computer_option}")
elif player_option == 'scissors' and computer_option == 'paper':
  print("Computer wins!")
  print(f"Computer chose {computer_option}")
elif player_option == 'rock' and computer_option == 'scissors':
  print("You win!")
  print(f"Computer chose {computer_option}")
elif player_option == 'scissors' and computer_option == 'rock':
  print("Computer wins!")
  print(f"Computer chose {computer_option}")

