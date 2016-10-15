##Sophia's drones are not soulless and stupid drones; they can make and have friends. In fact, they already are working for the their own social network just for drones! Sophia has received the data about the connections between drones and she wants to know more about relations between them.
##
##We have an array of straight connections between drones. Each connection is represented as a string with two names of friends separated by hyphen. For example: "dr101-mr99" means what the dr101 and mr99 are friends. Your should write a function that allow determine more complex connection between drones. You are given two names also. Try to determine if they are related through common bonds by any depth. For example: if two drones have a common friends or friends who have common friends and so on.
##
##network
##
##Let's look at examples:
##scout2 and scout3 have the common friend scout1 so they are related. super and scout2 are related through sscout, scout4 and scout1. But dr101 and sscout are not related.
##
##Input: Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.
##
##Output: Are these drones related or not as a boolean.
##
##Example:
##
##check_connection(
##    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
##     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
##    "scout2", "scout3") == True
##check_connection(
##    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
##     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
##    "dr101", "sscout") == False
##
##How it is used: This concept will help you find not too obvious connections with the building of bond networks. And how to work social networks.
##
##Precondition: len(network) ≤ 45
##if "name1-name2" in network, then "name2-name1" not in network
##3 ≤ len(drone_name) ≤ 6
##first_name and second_name in network.

def check_connection(network, first, second):
    reseau = list(network)
    startlink = []
    premier = first
    trouve = False
    present = True
    while present and not trouve and len(reseau) >= 1:
        present = False
        for link in reseau:
            if premier in link:
                startlink = link.split("-")
                startlink.remove(premier)
                premier = startlink[0]
                present = True
                reseau.remove(link)
                break
        if premier == second:
            trouve = True
    return trouve

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
