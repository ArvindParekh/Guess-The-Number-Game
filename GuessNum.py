# Exercise:- Take a predefined number and let the user guess it.

print("Hello Guys! Welcome to GuessTheNumber\nThe game is as follows:-\nIt can be played by two players. 1st player will decide a number and enter it and the 2nd player will try to guess it. The player will be given only 7 guesses before the game ends automatically. Try to guess it before they get over.\nAll the best, ROCK ON!")

player1_name = input("Enter a name for Player-1: ")
player2_name = input("Enter a name for player-2: ")
predef_num = int(input("Now it's turn for "+player1_name +" to select a number ("+player2_name+", Keep you eyes closed. No cheating!):\n"))
predef_chance = 7
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+player2_name+", It's your turn to play now.")
while(True):
    a = int(input("Enter a number\n"))
    predef_chance = predef_chance-1

    if predef_chance == 0 and a == predef_num:
        print("Congratulations! You have guessed the correct no\n")
        break
    elif predef_chance == 0:
        print("Sorry",player2_name, "you have run out of guesses. Game over!")
        print(player1_name,", nice job choosing the number!\n")
        break
    if a > predef_num:
        print("The number is greater, try lowering it")
        print("You have", predef_chance, "guesses left\n")
        continue
    elif a < predef_num:
        print("The number is smaller, try increasing it")
        print("You have", predef_chance, "guesses left\n")
        continue
    else:
        print("Congratulations",player2_name,"! You have guessed the correct no\n")
        break
        # again_ques = input("Do you want to play again?(Y/N)\n")
        # if again_ques=="Y":
        #     continue
        # elif again_ques=="N":
        #     break
        # else:
        #     print("Please enter Y or N only")
        # again_ques = input("Do you want to play again?(Y/N)\n")
        # if again_ques=="Y":
        #     continue
        # elif again_ques=="N":
        #     break
        # else:
        #     print("Please enter Y or N only")
        # Issue:- If user presses Y then the game starts but the guesses counts -1,-2,-3... so on
print("Thanks for playing the game!")


# can also add the total number to guesses it took to find the right answer
