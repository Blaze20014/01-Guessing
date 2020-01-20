import sys, random
import sys, time

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

compRandom = str(random.randint(1, 100))
correctGuess = False

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
    playerGuess = input("Enter a number from 1 to 100")

    if(playerGuess > compRandom):
        print("Your guess is too high")
    elif(playerGuess < compRandom):
       print("Your guess is too low")
    else:
       print("Your Correct, good job")
       correctGuess = True