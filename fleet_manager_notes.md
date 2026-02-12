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



