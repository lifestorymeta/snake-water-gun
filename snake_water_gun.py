import random

def game_results(user, comp):
    if(user==comp):
        return "Draw!"
    elif (user=="snake" and comp=="water") or \
         (user=="gun" and comp=="snake") or \
         (user== "water" and comp == "gun"):
         return "You Win!"
    else:
        return "You Lose!"
    
choices = ["snake", "water", "gun"]
comp_choice = random.choice(choices).lower()

print("Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!")
print(f"Choose one: {choices}")

user_choice = input("Enter your choice: ").lower()

if(user_choice not in choices):
    print("Invalid input. Please choose from Snake, Water, Gun.")

else:
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")
    print(game_results(user_choice, comp_choice))

