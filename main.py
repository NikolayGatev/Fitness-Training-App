from tkinter.font import names

from class_exercise import Exercise
from class_user import User
from class_workout import Workout

users = [User('Nik', 80, 160, 43, 'Lose weight'), User('Iv', 80, 160, 43, 'Lose weight')]
exercises = [Exercise('Squats', 'Up on stick', 'Hard'), Exercise('push-ups', 'Up on fload', 'Low'), Exercise('Lunges', 'for legs', 'Mid')]
workouts = [Workout('Intensive'), Workout('Easy'), Workout('Hard')]
goals = ['Keep in fit', 'Lose weight', 'Build muscle']

def get_user(name):
    return next((user for user in users if user.name == name), None)

def get_exercise(name):
    return next((ex for ex in exercises if ex.name == name))

def create_user(name, weight, height, age, goal):
    user = User(name, weight, height, age, goal)
    return user

def display_enter_menu():
    print("\n--- Welcome to the ---\n--- Fitness program ---")
    print("1. You have account")
    print("2. You would like to create new account")

    choice = int(input("Please! Enter your choice: "))
    return choice

def create_new_user():
    print("For your account we need your data:")

    name = input("Your name: ")
    weight = int(input("Your current weight in kilograms: "))
    height = int(input("Your height in centimeters:"))
    age = int(input("Your age in years: "))
    goal = input(f'Choose your fitness goals from next: {', '.join(goals)}: ')
    current_user = create_user(name, weight, height, age, goal)
    if get_user(name):
        print('Such user already exist')
        return
    users.append(current_user)
    print(f'Congratulations, you have account! Your data are: {current_user.display_info()}')

def update_your_data():
    name = input('Please enter your account name: ')
    user = get_user(name)
    if not user:
        print('Unknown name')
        return
    choice = input('If you want to change weight press 1\nIf you want to change fitness goal press 2\nyour choice is: ')
    if choice == '1':
        new_weight = int(input('Enter your new weight: '))
        user.update_weight(new_weight)
    elif choice == '2':
        new_goal = input(f'Enter your new goal from these ({', '.join(goals)}): ')
        user.update_goal(new_goal)

    print(f'your data are {user.display_info()}')

def create_new_exercise():
    name = input('Enter name on exercise: ')
    if get_exercise(name):
        print('This name already is used')
        create_new_exercise()
    description = input('Enter description on exercise: ')
    difficult = input('Enter difficult on exercise: ')
    ex = Exercise(name, description, difficult)
    exercises.append(ex)
    print(f'Your new exercise is {ex.display_exercise()}')

def create_new_workout():
    name = input('Enter name of new workout')

def choice_display_menu():
    """Display the main menu."""
    print("\n--- Fitness program ---")
    print("1. Create Account")
    print("2. change data in your account")
    print('3. Create new exercise')
    print('4. Create new Workout')
    print('5. Change workout')

    print("10. Exit")


    choice = int(input('Enter your choice: '))
    return choice


def main():
    while True:
        """Main function to run the fitness program."""
        choice = choice_display_menu()

        if choice == 1:
            create_new_user()
        elif choice == 2:
            update_your_data()
        elif choice == 3:
            create_new_exercise()
        elif choice == 4:
            create_new_worout()
        elif choice == 5:
            update_your_data()


main()