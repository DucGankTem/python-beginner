import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]
            #0        1         2      (number list)


while True:
    user_input = input ("Type Rock/paper/scissor or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissor"]:
        continue

    random_number = random.randint(0,2)
    #rock : 0 ; paper : 1 , scissor : 2
    computer_picks = options[random_number]
    print("computer picked", computer_picks + ".")

    if user_input == "rock" and computer_picks  == "scissor":
        print("you won!")
        user_wins += 1

    elif user_input == "paper" and computer_picks  == "rock":
        print("you won!")
        user_wins += 1

    elif user_input == "scissor" and computer_picks  == "paper":
        print("you won!")
        user_wins += 1
    else:
        print("you lose")
        computer_wins += 1
     


print("you won " , user_wins , "games!")
print("computer won " , computer_wins , "games!")

print ("Good bye!")


    
