from random import randint


def Game(word, letters):
    allowed_fails = int(input("How many fails do you want to allow before losing? "))
    attempts = 0
    correct_letters = []
    guessed_letters = []
    guessed = False

    while allowed_fails > 0:
        guess = input("Guess a letter: ").lower()
        attempts += 1
        if guess in letters:
            add_number = letters.count(guess)
            for n in range(add_number):
                correct_letters.append(guess)
            correct_letters.sort()
            print("Correct!\n")
        else:
            print("Not quite.\n")
            allowed_fails -= 1
        guessed_letters.append(guess)
        if correct_letters == letters:
            print(f"You got it! The word was {word}")
            guessed = True
            break
        print(f"Letters guessed: {guessed_letters}")
        print(f"Correct guesses: {correct_letters}\n")
    if guessed is False:
        print(f"You ran out of fails. The word was {word}")


def GetWordList():
    with open("AllowedWords.txt") as words:
        wordlist = words.readlines()
        word = wordlist[randint(0, len(wordlist))].lower()
    letters = list(word)
    letters.sort()
    return word, letters


def main():
    word, letters = GetWordList()
    Game(word, letters)


if __name__ == "__main__":
    print("Welcome to Hangman!\n--------------------")
    main()
    retry = input("Do you want to play again? (y/n)")
    if retry == "y":
        main()
    else:
        quit()
