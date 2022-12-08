import random
Count = 0
Mode = ""
while not (Mode == "P" or Mode == "R"):
    Mode = input("Select mode, choose if you want the computer to play randomly or perfectly. Please enter \"P\" for perfect inputs, or \"R\" for random inputs: ")
    print(Mode)
while Count <= 20:
    try:
        player_num = int(input("Select a number between 1-3: "))
        if not (player_num >= 1 and player_num <= 3):
            print ("Number was outside of range, please try again")
        else:
            Count += player_num
            if (player_num == 1):
                Com_Choice = 3
            if (player_num == 2):
                Com_Choice = 2
            if (player_num == 3):
                Com_Choice = 1
            if Mode == "R":
                Com_Choice = random.randint(1,3)
            if Count >= 21:
                print ("You went over 21. You Lost")
            else:
                Count += Com_Choice
                if Count >= 21:
                    print ("The computer went over 21. You Won!")
                else:
                    print ("The Computer chose the number " + str(Com_Choice) + ", the total is now " + str(Count))
    except ValueError:
        print ("Invalid value, please try again")
