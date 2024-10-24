from class_user import User

goals = ['Keep in fit', 'Lose weight', 'Build muscle']
def create_user(name, weight, height, age, goal):
    user = User(name, weight, height, age, goal)
    return user

def display_enter_menu():
    print("\n--- Welcome to the ---\n--- Fitness program ---")
    print("1. You have account")
    print("2. You would like to create new account")

    choice = int(input("Please! Enter your choice: "))
    return choice

def main():
    while True:
        choice = display_enter_menu()

        if choice == 1:
            pass
        if choice == 2:
            print("For your account we need your data:")

            name = input("Your name: ")
            weight = int(input("Your current weight in kilograms: "))
            height = int(input("Your height in centimeters:"))
            age = int(input("Your age in years: "))
            goal = input(f'Choose your fitness goals from next: {', '.join(goals)}: ')
            current_user = create_user(name, weight, height, age, goal)

main()