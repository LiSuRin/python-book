import random


def ask_number(question, low=1, high=100, step=1):
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response


def main():
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")
    # set the initial values
    the_number = random.randint(1, 100)
    guess = ask_number("Take a guess: ")
    tries = 1
    # guessing loop
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")

        guess = ask_number("Take a guess: ")
        tries += 1

    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")


main()
