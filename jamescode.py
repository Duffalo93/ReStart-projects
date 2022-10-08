# Importing the random module.
import random

# Bodypart ists to retrieve exercises from
back_list = ["Pull Up", "Bent-Over Row", "Single-Arm Dumbbell Row", "Lat Pulldown", "Seated back row"]
arms_list = ["Hammer Curl", "Cable Tricep Extension", "Barbell Bicep Curl", "Skull Crusher"]
shoulders_list = ["Dumbell Front Raise", "Military Press", "Reverse Fly", "Dumbell Lateral Raise" ]
legs_list = ["Squat", "Lunges", "Leg Extension", "Calf Raise", "Single Leg Curl"]
chest_list = ["Bench Press", "Dumbell Flyes", "Push up", "Dumbell Incline", "Dumbell Decline" ]


# Retrieves two random workouts from bodypart list
def exercise_to_complete(exercise_name):
    if(exercise_name == "Back"):
        exercise_back = random.sample(back_list, k=2)
        exercises_back = random.sample(back_list, k=2)
        for exercise_back in exercises_back:
            print(f"You will peform 3 sets of 8 reps of {exercise_back}")


    elif(exercise_name == "Arms"):
        exercise_arms = random.sample(arms_list, k=2)
        exercises_arms = random.sample(arms_list, k=2)
        for exercise_arms in exercises_arms:
            print(f"You will peform 3 sets of 8 reps of {exercise_arms}")

    elif(exercise_name == "Shoulders"):
        exercise_shoulders = random.sample(shoulders_list, k=2)
        exercises_shoulders = random.sample(shoulders_list, k=2)
        for exercise_shoulders in exercises_shoulders:
            print(f"You will peform 3 sets of 8 reps of {exercise_shoulders}")

    elif(exercise_name == "Chest"):
        exercise_chest = random.sample(chest_list, k=2)
        exercises_chest = random.sample(chest_list, k=2)
        for exercise_chest in exercises_chest:
            print(f"You will peform 3 sets of 8 reps of {exercise_chest}")

    elif(exercise_name == "Legs"):
        exercise_legs = random.sample(legs_list, k=2)
        exercises_legs = random.sample(legs_list, k=2)
        for exercise_legs in exercises_legs:
            print(f"You will peform 3 sets of 8 reps of {exercise_legs}")

    return

# -------------- MAIN LOOP -----------------

# Ask user for name
print("Kia ora! and welcome to the gym exercise randomizer! ")
name = input("What is your name? ")


# Ask user what body part they will be working out and give a set and rep
bodypart = input(f"Hello, {name} , What body part do you want to workout? Choose from Back, Legs, Arms, Shoulders, Chest. ")
exercise_to_complete(exercise_name=bodypart)

# Allows option to choose another bodypart or to end your workout

running = True
while(running):
    is_running = input(f"Press Y to choose next bodypart, Press N to finish your workout ")
    if(is_running == "Y" or is_running == "y"):
        print(f"Looping back to the beggining!")
        continue
    if(is_running == "N" or is_running == "n"):
        print(f"Exercises done! Goodbye!")
        running = False
    else:
        print(f"Invalid input, please try again. Y or N? ")
        continue

