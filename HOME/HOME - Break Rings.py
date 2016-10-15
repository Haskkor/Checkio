##A blacksmith gave his apprentice a task, ordering them to make a selection of rings. The apprentice is not yet skilled in the craft and as a result of this, some (to be honest, most) of rings came out connected together. Now he’s asking for your help separating the rings and deciding how to break enough rings to free so as to get the maximum number of rings possible.
##
##All of the rings are numbered and you are told which of the rings are connected. This information is given as a sequence of sets. Each set describes the connected rings. For example: {1, 2} means that the 1st and 2nd rings are connected. You should count how many rings we need to break to get the maximum of separate rings. Each of the rings are numbered in a range from 1 to N, where N is total quantity of rings.
##
##In the above image you can see the connections: ({1,2},{2,3},{3,4},{4,5},{4,6},{6,5}). The optimal solution here would be to break 3 rings, making 3 full and separate rings. So the result is 3.
##
##Input: Information about the connected rings as a tuple of sets with integers.
##
##Output: The number of rings to break as an integer.
##
##Example:
##
##break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {6, 5})) == 3
##
##How it is used: This model specializes in optimizing something with specific conditions. Using the basic concepts, you could create a model for improving a transportation grid.

Precondition: all(len(s) == 2 for s in rings)
sorted(reduce(set.union, rings)) == list(range(1, max(reduce(set.union, rings)) + 1))

import copy
​
def tuple_to_list(rings):
    """ Transforms the given tuples into lists. """
    temp_list = []
    for link in rings:
        temp_list.append(list(link))
    return temp_list
    
def get_min_ring(rings):
    """ Create a dict with the number of link for each ring and returns the
    ring with the least link. """
    link_count = dict()
    for link in rings:
        for elem in link:
            if elem in link_count:
                link_count[elem] += 1
            else:
                link_count[elem] = 1
    # Trouve la valeur minimum du dictionnaire
    min_value = min(link_count.items(), key=lambda x: x[1])[1]
    # Fais une liste de toutes les clefs dont la valeur est égale à la valeur min et la trie
    sorted_values = [key for key, value in link_count.items() if value == min_value]
    sorted_values.sort()
    return sorted_values[0]
    
def get_linked_rings(ring,rings):
    """ Returns a ring linked to the ring with minimum links. """
    temp_list=[]
    for link in rings:
        if ring in link:
            temp = copy.deepcopy(link)
            temp.remove(ring)
            temp_list.append(temp[0])
    temp_list.sort()
    return temp_list[0]
    
def break_ring(list_links,ring_to_destroy):
    """ Break the selected ring and fill the separate rings list. """
    temp_list = []
    for link in list_links:
        if ring_to_destroy not in link:
            temp_list.append(link)
    return temp_list
​
def break_rings(rings):
    """ Main function. """
    broken_rings = 0
    list_links = tuple_to_list(rings)
    while len(list_links) > 0:
        ring_min = get_min_ring(list_links)
        ring_to_destroy = get_linked_rings(ring_min,list_links)
        list_links = break_ring(list_links,ring_to_destroy)
        broken_rings += 1
    return broken_rings     
        
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({1, 9}, {1, 2}, {8, 5}, {4, 6}, {5, 6}, {8, 1}, {3, 4}, {2, 6}, {9, 6}, {8, 4}, {8, 3}, {5, 7}, {9, 7}, {2, 3}, {1, 7})) == 5, "Very long chain"
    assert break_rings(({3, 4}, {5, 6}, {2, 7}, {1, 5}, {2, 6}, {8, 4}, {1, 7}, {4, 5}, {9, 5}, {2, 3}, {8, 2}, {2, 4}, {9, 6}, {5, 7}, {3, 6}, {1, 3})) == 5, "Stfu"
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 2}, {1, 6}, {6, 7}, {7, 8}, {8, 9}, {9, 6}, {1, 10}, {10, 11}, {11, 12}, {12, 13}, {13, 10}, {1, 14}, {14, 15}, {15, 16}, {16, 17}, {17, 14})) == 8, "Wth"
