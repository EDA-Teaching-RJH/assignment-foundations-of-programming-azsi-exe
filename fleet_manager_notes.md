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

4. add_member(names, ranks, divs, ids) function
def add_member(names, ranks, divs, ids):
    print("\n--- ADD MEMBER ---")
    new_name = input("Name: ").strip()
    new_rank = input("Rank: ").strip()
    new_division = input("Division: ").strip()
    new_id = input("ID: ").strip()

    if new_rank not in allowed_ranks:
        print("Rank invalid")
        print("Please choose from: ")
        for r in allowed_ranks:
            print(r)
        return
        
    if new_division not in allowed_divisions:
        print("Division invalid")
        print("Please choose from: ")
        for d in allowed_divisions:
            print(d)
        return
    
    if new_id in ids:
        print("The list of ID's below have already been created: ")
        for i in ids:
            print(i)
        return
    
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_division)
    ids.append(new_id)

    print("New member added successfully")
- The add member function allows user to add new crew members. User asked for new memeber details. If members rank or division doesn't match list, user is reminded what was available. if id was similar to previously used ids attached to other crew members, it would remind user ids that are used.

5. update_rank(names, ranks, ids) function
def update_rank(names, ranks, ids):
    print("\n--- UPDATE RANK ---") # update member rank

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

    print(f"You have officially updated {name}'s rank to {new_rank}")
- Update rank was added to allow user to update any of the members ranks by first identifying the name in the names list. The system would find the positioning of the name in the list, and use it to identify the name and rank (as they are parallel lists). Once the user inputs a new rank (if it is included in the allowed ranks), it would update. If nto user would be reminded of ranks allowed.

6. display_roster(names, ranks, divs, ids) function
def display_roster(names, ranks, divs, ids):
    print("--- DISPLAY ROSTER ---") # update member rank
    print("--------------------------------")

    for i in range(len(names)): #displays crew details in parallel lists
        print(names[i], "-", ranks[i], "-", divs[i], "-", ids[i])
- Display roster created to display all crew members details currently within the parallel lists, using a for loop.

7. search_crew(names, ranks, divs, ids) function
def search_crew(names, ranks, divs, ids):
    print("--- SEARCH CREW ---")

    search_term = input("Enter search term: ").strip()

    for i in range(len(names)):
        if search_term == names[i]:
            print(names[i], "-", ranks[i], "-", divs[i], "-", ids[i])
            return
        
        print(f"Nothing matches {search_term}.")
- This menu option allows user to search name and output their details

8. filter_by_division(names, divs) function
def filter_by_division(names, divs):
    print("--- FILTER BY DIVISION ---")

    division = input("Enter division: ").strip()

    if division not in allowed_divisions:
        print("Division invalid")
        print("Please choose from: ")
        for d in allowed_divisions:
            print(d)
        return
    
    for i in range(len(names)): # loops through list, prints crew members
        if divs[i] == division:
            print(names[i])
- This function allows user to filter through parallel lists to find crew members within the division searched for.

9. calculate_payroll(ranks) function
def calculate_payroll(ranks):
    total = 0 

    for rank in ranks: # assign credit values to each rank
        if rank == "Captain":
            total += 1600
        elif rank == "Commander":
            total+= 1100
        elif rank == "Commander":
            total+= 700
        elif rank == "Commander":
            total+= 400
        elif rank == "Commander":
            total+= 200
        elif rank == "Commander":
            total+= 100
        
    return total # adds total
- Function created to assign credit value for each crew member, based on their rank.