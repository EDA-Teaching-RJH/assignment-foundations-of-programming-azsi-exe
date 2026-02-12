1. Ranks and divisions lists
ranks = [
    "Captain",
    "Commander",
    "Lt. Commander",
    "Lieutenant",
    "Lt. Junior Grade",
    "Ensign"
]

divisions = [
    "Command",
    "Operations",
    "Sciences"
]
- I added lists for ranks and divisions so only these values in the lists are allowed and can restrict users from typing invalid inputs. This is also to keep the same values used anywhere in the program instead of repeating in each function.

2. init_database() function
def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Spock"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["01", "02", "03", "04", "05"]
    return names, ranks, divisions, ids
- This is the start data with 5 Star trek characters and their ranks, divisions, and ids.

3. display_menu() function
def display_menu(user_name):
    if user_name == " ":
        user_name = input("What is your name?: ").strip()

    print ("\n-------------------------")
    print("WELCOME TO FLEET COMMAND")
    print("WELCOME BACK: ", user_name)
    print ("\n-------------------------")

    print("\n--- MENU ---")
    print("1. Add member")
    print("2. Remove member")
    print("3. Update rank")
    print("4. Display roster")
    print("5. Search crew")
    print("6. Filter by division")
    print("7. Calculate payroll")
    print("8. Count officers")
    print("9. Exit")

    option = input("Please choose an option").strip()
    return option
- This updated display menu incorporates all functions created. Option for user to also create a username, addressed by the system, has also been created.

