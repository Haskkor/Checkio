##Nicola is taking a much needed vacation. He'll be backpacking around some lesser-known countries. Each has its own unique currency.
##
##When making purchases, Nicola would like to use the minumum number of coins possible. For example, Outer Leftopia has coins with denomination 1, 3, and 5 shillings. He wants to buy a souvenir that costs 13 shillings. He can do that using two 5 shilling coins and one 3 shilling coin.
##
##You can assume Nicola has access to an infinite number of coins of each denomination. (He has a large bank account and access to an ATM).
##
##Input: Two arguments. The first argument is an int: the price of the purchase. The second is a list of ints: the denominations of available coins.
##
##Output: int. The minimum number of coins Nicola can use to make the purchase. If the price cannot be made with the available denominations, return None.
##
##Example:
##
##checkio(8, [1, 3, 5]) == 2
##checkio(12, [1, 4, 5]) == 3
##
##How it is used: Besides helping Nicola make change, this is an example of a problem in combinatorial optimization.
##
##Precondition: Inputs are all positive integers.

def checkio(price,coins):
    list_result = set(coins)
    for i in range(2,price+1):
        list_result = {number + coin for number in list_result \
            for coin in coins}
        if price in list_result:return i
    
print(checkio(8, [1, 3, 5]))
print(checkio(12, [1, 4, 5]))
print(checkio(9658, [1,6,7,456,678]))
print(checkio(123456, [1,6,7,456,678]))

###########################
### TECHNIQUE ITERATIVE ###
###########################

##def checkio(price,coins):
##    coins.reverse()
##    result = []
##    while len(coins) > 0:
##        sum_coins,nbr_coins = 0,0
##        for coin in coins:
##            while sum_coins + coin <= price:
##                print(sum_coins)
##                sum_coins += coin
##                nbr_coins += 1
##                if result:
##                    if nbr_coins >= min(result):
##                        break
##        coins = coins[1:]
##        if sum_coins == price:result.append(nbr_coins)
##        print("")
##        print(nbr_coins)
##        print("")
##    if result:return min(result)
##    else:return None
##
##print(checkio(9658, [1,6,7,456,678]))

##################################
### TECHNIQUE ULTIME (CHECKIO) ###
##################################

##def checkio(price, denoms):
##    sums = set()
##    for number in range(1, price + 1):
##        sums = {s + d for s in sums for d in denoms} or set(denoms)
##        if price in sums: return number
##
##print(checkio(9658, [1,6,7,456,678]))

#############################
### TECHNIQUE PERMUTATION ###
#############################

##import itertools
##
##def calc(price,coins):
##    sum = 0
##    for coin in coins:
##        sum += price // coin
##        price = price % coin
##    if price == 0:
##        return sum
##    else:
##        return 0
##
##def checkio(price,coins):
##    permut_coins = [x for x in itertools.permutations(coins)]
##    result = []
##    for permut in permut_coins:
##        result.append(calc(price,permut))    
##    if min(result) == 0:return None
##    else:return min(result)

#############################
### TECHNIQUE RECURSIVITE ###
#############################

##def subset_sum(numbers,target,result,partial=[]):
##    s = sum(partial)
##    if s == target: 
##        result.append(len(partial))
##    if result:
##        if len(partial) > min(result):
##            return
##    if s >= target:
##        return
##    for i in range(len(numbers)):
##        n = numbers[i]
##        subset_sum(numbers,target,result,partial + [n])
##        remaining = numbers[i+1:]
##        subset_sum(remaining,target,result,partial + [n])
##
##def checkio(price,coins):
##    result = []
##    coins.reverse()
##    subset_sum(coins,price,result)
##    if result:return min(result)
##    else:return None
