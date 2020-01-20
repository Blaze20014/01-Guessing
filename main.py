import sys, random
import sys, time

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

compRandom = random.randint(1, 100)
correctGuess = False
guesses = 0

print("Running GLaDOS_Installer_V1.14.2")
time.sleep(1)
print("GLaDOS booting up...")
time.sleep(1)
print("GLaDOS: Hello player; I see you have been put under my supervision")
time.sleep(3)
print("GLaDOS: Allow me to introduce myself: ")
time.sleep(3)
print("I am the Genetic Lifeform and Disk Operating System or GLaDOS for short")
time.sleep(3)
print("My main protocol is to administer tests to those in my supervision")
time.sleep(3)
print("and it looks like that is you right now")
time.sleep(3)
print("So lets begin with a simple test: a guessing game")
time.sleep(3)
print("The rules are simple; I'll think of a number and you will guess it")
time.sleep(3)
print("... or try to at least")
time.sleep(3)

while(correctGuess == False):
    playerGuess = input("Enter a number from 1 to 100: ")

    if(int(playerGuess) > compRandom):
        print("Your guess is too high")
        guesses = guesses + 1
    elif(int(playerGuess) < compRandom):
        print("Your guess is too low")
        guesses = guesses + 1
    elif(int(playerGuess) == compRandom):
        print("Your Correct")
        guesses = guesses + 1
        correctGuess = True

time.sleep(2)
print("GLaDOS: Congratulations... You Win... I guess")
time.sleep(3)
print("Lets see how many guesses it took: ")
time.sleep(2)
if(guesses == 1):
    print("I'd applaud you for getting it in one guess")
elif(guesses > 5):
    print("Haha, you fool. You took an absurd " + str(guesses) + " guesses to reach a simple number...")
else:
    print("You did decent I guess what with " + str(guesses) + " guesses")

print("I'll come back with another test soon enough")