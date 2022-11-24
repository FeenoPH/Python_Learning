orig_word = "rainbow".lower()
word = orig_word
letters_left = orig_word
letters_guessed = ""
blank = "_"
blanks_in_word = blank * word.__len__()
guesses_left = 5
word = list(word)
completed = False

print(blanks_in_word)

while completed is False:
    invalid_guess = False
    if completed is False:
        print("You have " + str(guesses_left) + " guesses left.")
        user_guess = (input("Enter a letter: ")).lower()

        if user_guess.__len__() != 1:
            print("Invalid guess, please try again")
            invalid_guess = True
        if user_guess in letters_left and invalid_guess is False:
            letters_left = letters_left.replace(user_guess, "")
            number_of_occur = int(word.count(user_guess))
            for i in range(number_of_occur):
                point_of_guess = word.index(user_guess)
                blanks_in_word = blanks_in_word[:point_of_guess] + user_guess + blanks_in_word[point_of_guess + 1:]
                word[point_of_guess] = ""
            print("You got a letter!")
        elif user_guess not in letters_left and invalid_guess is False:
            if user_guess in letters_guessed:
                print("You've already guessed that letter")
            else:
                print("Nice try, but that letter is not in the word")
                guesses_left -= 1
        print(blanks_in_word)
        if letters_left == "":
            print("Congratulations, you guessed the word!")
            completed = True
        letters_guessed = letters_guessed + user_guess
    if letters_left != "" and guesses_left == 0:
        print("You ran out of guesses. The word was " + orig_word + ". Maybe next time")
        completed = True
