##Do you know how to play Prime Palindrome Golf? You are given a number and your challenge is to find the closest palindromic prime number that greater than what you were given.
##
##A palindromic number or numeral palindrome is a number that remains the same when its digits are reversed, such as 79197. These numbers appear to be symmetrical. 
##A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In this task you will be given an positive integer. You should find the closest integer that:
##- is greater than the given number;
##- is prime;
##- is palindromic.
##For example: for the number 13, the closest greater palindromic prime is 101. Or, for the number is 2, the answer is 3, because any one-digit number is a palindrome.
##
##We have one more rule for this challenge. This is a code golf mission and your main goal is to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code. For reference, scoring is based on the number of characters used. 250 characters is the maximum allowable and it will earn you zero points. For each character less than 250, you earn 1 point. For example for 200 character long code earns you 50 points.
##
##Important: We are using default recursion limit (100). So don't try to solve this mission with recursion.
##
##Input: A number as an integer.
##
##Output: The closest greater palindromic prime as an integer.
##
##Example:
##
##golf(2) == 3
##golf(13) == 101
##golf(101) == 131
##
##How it is used: Prime numbers are very useful for many CS areas, however; this task is not about elegant or performance code. This is about hacks and tricks in python which help you to shorten your code. You don't need to use this in production, but it can help for deeper comprehension of Python.
##
##Precondition: 0 < number < 98689

def golf(n):
    n+=1
    while not all(n%i for i in range(2,n)) or str(n)!=str(n)[::-1]:n+=1
    return n

# str(n)!=str(n)[::-1] : fait une copie de l'inverse de la liste et la
# compare à la liste originale

#def all(iterable):
#    for element in iterable:
#        if not element:
#            return False
#    return True

print(golf(101))
