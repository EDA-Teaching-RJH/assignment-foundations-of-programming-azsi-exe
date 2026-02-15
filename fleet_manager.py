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
    names = ["Picard", "Riker", "Data", "Worf", "Spock"] # created initial database of crew members
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["01", "02", "03", "04", "05"]
    return names, ranks, divs, ids

def display_menu(user_name):
    print ("-------------------------")
    print("WELCOME TO FLEET COMMAND")
    print("WELCOME BACK: ", user_name)
    print ("-------------------------")

    print("--- MENU ---") # menu and options available to user
    print("1/ Add member")
    print("2/ Remove member")
    print("3/ Update rank")
    print("4/ Display roster")
    print("5/ Search crew")
    print("6/ Filter by division")
    print("7/ Calculate payroll")
    print("8/ Count officers")
    print("9/ Exit")

    option = input("Select option: ").strip() # .strip() = removes any accidental spaces
    return option

def add_member(names, ranks, divs, ids):
    print("--- ADD MEMBER ---") # new member info
    new_member_name = input("Name: ").strip().capitalize()
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

def remove_member(names, ranks, divs, ids):
    print("--- REMOVE MEMBER ---")

    remove_id = input("Enter the member ID you want to remove: ").strip()

    if remove_id not in ids: # checks if the ID the user entered is within the list. if not, user is shown the list of IDs available.
        print(f"{remove_id} not valid.")
        print("Please choose an ID from: ")
        for i in ids:
            print(i)
        return
    
    idx = ids.index(remove_id)

    print("Are you sure you want to remove: ") # asks for confirmation to user
    print(names[idx], "-", ranks[idx], "-", divs[idx], "-", ids[idx])

    confirm = input("Is this correct? (Yes/No): ").strip().capitalize() 

    if confirm == "Yes":
        names.pop(idx) # removes index position in the list, deleting the member.
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Member removed successfully.")
    else:
        print("Cancelled.")


def update_rank(names, ranks, ids):
    print("--- UPDATE RANK ---") # update member rank

    name = input("Enter member name: ").strip().capitalize() # asks user for name

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
        if search_term.lower() in names[i].lower():
            print(names[i], "-", ranks[i], "-", divs[i], "-", ids[i])
            return
        
    print(f"Nothing matches {search_term}.")

def filter_by_division(names, divs):
    print("--- FILTER BY DIVISION ---")

    division = input("Enter division (Command/ Operations/ Security/ Sciences): ").strip()

    if division not in allowed_divisions:
        print("Division invalid")
        print("Please choose from: ")
        for d in allowed_divisions:
            print(d)
        return
    
    for i in range(len(names)): # loops through list, prints crew members
        if divs[i] == division:
            print(names[i])

def calculate_payroll(ranks):
    total = 0 

    for rank in ranks: # assign credit values to each rank
        if rank == "Captain":
            total += 1600
        elif rank == "Commander":
            total+= 1100
        elif rank == "Lt. Commander":
            total+= 700
        elif rank == "Lieutenant":
            total+= 400
        elif rank == "Lt. Junior Grade":
            total+= 200
        elif rank == "Ensign":
            total+= 100
        
    return total # adds total

def count_officers(ranks):
    count = 0

    for rank in ranks: # count variable gains 1 per commander + captain within the crew.
        if rank == "Captain" or rank == "Commander":
            count += 1

    return count

def main():
    names, ranks, divs, ids = init_database() # Creates parallel lists with starting data
    user_name = input("What is your name?: ").strip().capitalize()

    while True: # Loop will run until user selects 9
        option = display_menu(user_name) # Shows menu and stores users choice

        if option == "1":
            add_member(names, ranks, divs, ids)
        elif option == "2":
            remove_member(names, ranks, divs, ids)
        elif option == "3":
            update_rank(names, ranks, ids)
        elif option == "4":
            display_roster(names, ranks, divs, ids)
        elif option == "5":
            search_crew(names, ranks, divs, ids)
        elif option == "6":
            filter_by_division(names, divs)
        elif option == "7":
            total = calculate_payroll(ranks)
            print(f"Total payroll: {total}")
        elif option == "8":
            total = count_officers(ranks)
            print(f"Total officers: {total}")
        elif option == "9":
            print("Goodbye.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()