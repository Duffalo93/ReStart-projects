# Importing the random module.
import random

# defines back list to choose from
#def back_list():
 #   pass

# back workouts within list
back_list = ["Pull Up", "Bent-Over Row", "Single-Arm Dumbbell Row", "Lat Pulldown", "Seated back row"]

# Ask user for name
name = input("Kia ora, what is your name? ")
print ("Kia ora " + name)

# Ask user what body part they will be working out

bodypart = input("What body part do you want to workout?")
print ("Sweet, you will be working out " + bodypart)

if bodypart == 'Back':
    exercise = random.choice(back_list)
    print(exercise) 





