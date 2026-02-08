n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    

    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1     # Stops loop once loading variable hits 5

    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  
            print("Current Crew List:")
            
            # only 4 options (starting from 0), therefore changing this to length of the actual list would fix any errors.
            for i in range(len(n)):
                print(n[i] + " - " + r[i] + " - " + d[i]) # prints division as well
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
           # if only the name list is updated, it causes the lists to be different lengths, causing an error when viewing as it relies on the lists being parallel (pulling data for 7th crew member: n[6] + r[6] + d[6] would only be possible if lists were updated correctly)
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           

            # Creating if statement prevents crash if the name entered does not exist in the list.
            if rem in n:
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print("Crew member was not found.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": # separates rank into 2 seprate values, as it is checking "Commander" by itself, not as a rank
                    count = count + 1
            print("High ranking officers: ", count) # count is an int, not a string, therefore a comma is used. otherwise + would be used. # or "print("High ranking officers: " + str(count))""
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()