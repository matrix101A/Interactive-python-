import simpleguitk as simplegui
import random

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
number = 0
r = 100
limit = 7
count = 0


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global number
    global r
    number = random.randint(0, r)
    print("Range is 0 to " + str(r) + "\nStart Guessing!")


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global r
    global limit
    r = 100
    limit = 7
    count
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global r
    global limit
    limit = 12
    r = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    global count
    global limit
    count += 1
    if (count >= limit):
        print("You have exhausted your guesses.Starting new game....")
        count = 0
        new_game()
    else:
        print("Gussed Number is: " + str(guess))
        global number
        if (number > int(guess)):
            print("Higher !\n" + str(limit - count) + " guesses remain")
        elif (number < int(guess)):
            print("Lower !\n" + str(limit - count) + " guesses remain")
        else:
            print("Correct answer ! \n\nStarting New game")
            count = 0
            new_game()


# create frame

frame = simplegui.create_frame("Guess The number", 200, 200)
# register event handlers for control elements and start frame
frame.add_button("Range:0-100", range100)
frame.add_button("Range:0-1000", range1000)
frame.add_input("Enter Your guess !", input_guess, 100)

# call new_game
frame.start()
new_game()

# always remember to check your completed program against the grading rubric
