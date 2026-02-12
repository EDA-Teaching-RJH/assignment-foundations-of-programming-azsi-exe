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
    "Security",
    "Sciences"
]

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Spock"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["01", "02", "03", "04", "05"]
    return names, ranks, divisions, ids

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




    