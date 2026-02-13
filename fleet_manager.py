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
    if user_name == " ": # .strip() so that user can't have a name with spaces or nothing, e.g. "   ", or ""
        user_name = input("What is your name?: ").strip()

    print ("-------------------------")
    print("WELCOME TO FLEET COMMAND")
    print("WELCOME BACK: ", user_name)
    print ("-------------------------")

    print("--- MENU ---")
    print("1/ Add member")
    print("2/ Remove member")
    print("3/ Update rank")
    print("4/ Display roster")
    print("5/ Search crew")
    print("6/ Filter by division")
    print("7/ Calculate payroll")
    print("8/ Count officers")
    print("9/ Exit")

    option = input("Select option: ").strip()
    return option

def add_member(names, ranks, divs, ids):
    print("--- ADD MEMBER ---") # new member info
    new_member_name = input("Name: ").strip()
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
    names.append(new_member_name)
    ranks.append(new_rank)
    divs.append(new_division)
    ids.append(new_id)

    print(f"Welcome to the crew, {new_member_name}.")

def update_rank(names, ranks, ids):
    print("--- UPDATE RANK ---") # update member rank

    name = input("Enter member name: ").strip() # asks user for name

    if name not in names: # defult output if name does not exist in the system
        print("Name not valid.")
        return
    
    idx = names.index(name) # finds position of the name in the list

    new_rank = input("Enter new rank: ").strip()

    if new_rank not in allowed_ranks: # check if rank matches list
        print("Rank invalid")
        print("Please choose from: ")
        for r in allowed_ranks:
            print(r)
        return
    
    ranks[idx] = new_rank # makes sure the new rank updates in the same index as previous rank

    print(f"You have officially updated {name}'s rank to {new_rank}.")

def display_roster(names, ranks, divs, ids):
    print("--- DISPLAY ROSTER ---") # update member rank
    print("--------------------------------")

    for i in range(len(names)): #displays crew details in parallel lists
        print(names[i], "-", ranks[i], "-", divs[i], "-", ids[i])

def search_crew(names, ranks, divs, ids):
    print("--- SEARCH CREW ---")

    search_term = input("Enter search term: ").strip()

    for i in range(len(names)):
        if search_term == names[i]:
            print(names[i], "-", ranks[i], "-", divs[i], "-", ids[i])
            return
        
        print(f"Nothing matches {search_term}.")


