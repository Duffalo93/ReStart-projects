# Importing the random module.
import random


# Ask user for name
print ("Kia ora! and welcome to the gym exercise randomizor! ")
name = input("What is your name? ")
# Ask for goal
#goal = input("Type 1 to lose weight or 2 to gain muscle")

# Lists to retrieve exercises from
back_list = ["Pull Up", "Bent-Over Row", "Single-Arm Dumbbell Row", "Lat Pulldown", "Seated back row"]
arms_list = ["Hammer Curl", "Cable Tricep Extension", "Barbell Bicep Curl", "Skull Crusher"]
legs_list = ["Squat", "Lunges", "Leg Extension", "Calf Raise", "Single Leg Curl"]
shoulders_list = ["Dumbell Front Raise", "Military Press", "Reverse Fly", "Dumbell Lateral Raise" ]
chest_list = ["Bench Press", "Dumbell Flyes", "Push up", "Dumbell Incline", "Dumbell Decline" ]


# Ask user what body part they will be working out and give a set and rep
bodypart = input("Hello " + name + ", What body part do you want to workout? Choose from Back, Legs, Arms, Shoulders, Chest! ")

if bodypart == 'Back':
    exercise = random.choice(back_list)
    print("You will peform the " + exercise + " 3 sets of 8 reps") 

if bodypart == 'Arms':
    exercise = random.choice(arms_list)
    print("You will peform the " + exercise + " 3 sets of 8 reps") 

if bodypart == 'Legs':
    exercise = random.choice(legs_list)
    print("You will peform the " + exercise + " 3 sets of 8 reps") 

if bodypart == 'Shoulders':
    exercise = random.choice(shoulders_list)
    print("You will peform the " + exercise + " 3 sets of 8 reps") 

if bodypart == 'Chest':
    exercise = random.choice(chest_list)
    print("You will peform the " + exercise + " 3 sets of 8 reps")  






