# Rock Paper Scissors Game

import random
computer_choice = random.choice(["r" , "p" ,"s"])
user_choice = input("Rock, paper, scissors? (r/p/s): ")
if user_choice == ("r") and computer_choice == 'r':
    print("Computer chose: 👊 ")
    print("Draw")
elif user_choice == 'r' and computer_choice == 'p':
    print("Computer chose: 🖐️")
    print("You lose")
elif user_choice == 'r' and computer_choice == 's':
    print("Computer chose: ✌️")
    print("You win")
elif user_choice == 's' and computer_choice == 's':
    print("Computer chose: ✌️")
    print("Draw")
elif user_choice == 's' and computer_choice == 'r':
    print("Computer chose: 👊")
    print("You lose")
elif user_choice == 's' and computer_choice == 'p':
    print("Computer chose: 🖐️")
    print("You win")
elif user_choice == 'p' and computer_choice == 'p':
    print("Computer chose: 🖐️")
    print("Draw")
elif user_choice == 'p' and computer_choice == 's':
    print("Computer chose: ✌️")
    print("You lose")
elif user_choice == 'p' and computer_choice == 'r':
    print("Computer chose: 👊")
    print("You win")
else:
    print("Invalid choice")
