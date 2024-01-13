import random

print("Let's play this game Rock, Paper, Scissor")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
User_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(game_images[User_choice])
Computer_choice = random.randint(0, 2)
print(Computer_choice)
print(game_images[Computer_choice])
if User_choice >= 3 or User_choice <0:
    print("It's an invalid number")
elif User_choice > Computer_choice:
    print("You Win")
elif Computer_choice > User_choice:
    print("You Lose")
elif User_choice == 0 and Computer_choice == 2:
    print("You Win")
elif User_choice == 2 and Computer_choice == 1:
    print("You Lose")
elif User_choice == Computer_choice:
    print("It's a Tie")
