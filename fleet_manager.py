allowed_ranks = [
    "Captain",
    "Commander",
    "Lt. Commander",
    "Lieutenant",
    "Lt. Junior Grade",
    "Ensign"
]

allowed_divisions = [
    "Command",
    "Operations",
    "Security",
    "Sciences"
]

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Spock"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["01", "02", "03", "04", "05"]
    return names, ranks, divs, ids

def display_menu(user_name):
    if user_name == " ": # .strip() so that user can't have a name with spaces, e.g. "   "
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

    option = input("Select option: ").strip()
    return option

def add_member(names, ranks, divs, ids):
    print("\n--- ADD MEMBER ---") # new member info
    new_name = input("Name: ").strip()
    new_rank = input("Rank: ").strip()
    new_division = input("Division: ").strip()
    new_id = input("ID: ").strip()

    if new_rank not in allowed_ranks: # check if rank matches list
        print("Rank invalid")
        print("Please choose from: ")
        for r in allowed_ranks:
            print(r)
        return
        
    if new_division not in allowed_divisions: # check if division matches list
        print("Division invalid")
        print("Please choose from: ")
        for d in allowed_divisions:
            print(d)
        return
    
    if new_id in ids: # check is id does not match previously assigned ids
        print("The list of ID's below have already been created: ")
        for i in ids:
            print(i)
        return
    
    # members added to parallel lists
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_division)
    ids.append(new_id)

    print("New member added successfully")

