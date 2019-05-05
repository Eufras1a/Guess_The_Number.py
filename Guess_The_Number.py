from random import randint
from sys import exit 

guess = 0
counter = 0  #  Counter for counting the number of guesses
a = 1        # initial range of guess
b = 20       # final range of guess

# Welcome Player
def welcome():
    print("What is your name ?")
    player = input()
    print(f'Hello, {player}!!!')

# Main code of the Game
def play():
    global counter, guess
    number = randint(a, b)
    counter = 0
    print(f'Guess what number i am thinking between {a} and {b} : ', end = '')
    guess = get_int()

    while(True):
        counter += 1

        if(guess == number):
            break
        elif(guess > number):
            print('The guess is too high')
        elif(guess < number):
            print('The guess is too low')
        else:
            print("error ?")
        
        print("Try Another Guess : ", end = '')
        guess = get_int()

def get_int():
    while True: 
        try:
            x = int(input())
            if(x >= 0):
                return x
            else:
                print('Enter +ve integer value : ', end = '')
        except ValueError:
            print("Not an integer, please enter an integer value : ", end = '')
       

def win():
    print("CONGRATULATIONS!!!!")
    print(f"You have successfuly cleared this game in {counter} guesses")

def win_alt():
    print("Holy Guacamoli!!!")
    print("What a guess!!!!")
    print('Just in one guess!!!!')
    print('YOU WIN THIS GAME!!!!!')
    exit()

if __name__ == "__main__":
    welcome()

    while(True):
        play()
        if(counter == 1):
            win_alt()
        else:
            win()

        again = input('press y/yes to play again: ').lower()

        if(again == 'y' or again == 'yes'):
            continue
        else:
            exit()