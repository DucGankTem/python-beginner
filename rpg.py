name = input("type your name here: ")

print("Welcome ", name, " to my first rpg game!")

answer = input("you are on the road, it has come to an end and you can go left or right. which way you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you want to walk away for swim accross. Type 'swim' or 'walk': ")

    if answer == "swim":
        print("you swim accross, you've been eaten by pussy")

    elif answer == "walk":
        print("you walk many miles, ran out of water, you lose the game")
    else:
        print("Invalid answer. You lose nigga")

elif answer == "right":
    answer = input("well well you walk right and you found something strange!. Type 'f' to interact ")
    if answer == "f":
        print("You found Huong! She's yours now")
    else:
        print("She eat yo ass. You lose")


else:
    print('not a valid option. you lose.') 

print("thank you for trying!", name)