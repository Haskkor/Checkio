##Do you remember the "Univocalic Fecterel Golf" mission? In this mission, you'll need use the same skills but with liiiittle tweak: "a" ⇄ "e".
##
##In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.
##
##Write a function named "a_factaral" which calculates the factorial without using these letters in code: "eiou".
##
##We have one more rule for this challenge. This is a code golf mission and your main goal is to make your code as short as possible. The shorter your code, the more points you earn. Your score for this mission is dynamic and directly related to the length of your code. For reference, scoring is based on the number of characters used. 250 characters is the maximum allowable and it will earn you zero points. For each character less than 250, you earn 1 point. For example for 150 character long code earns you 100 points.
##
##Input: A number as integer.
##
##Output: The factorial as an integer.
##
##How it is used: This is about hacks and tricks in python which help you to shorten your code. You don't need to use this in production, but it can help for deeper comprehension of Python.
##
##Preconditions: 0 ≤ n < 100

a_factaral=lambda n:((n!=0 and n*a_factaral(n-1))+(0,1)[n==0])

# this assertion should be stripped after self-testing.
if __name__ == '__main__':
    assert a_factaral(0) == 1, "Zero"
    assert a_factaral(1) == 1, "One"
    assert a_factaral(2) == 2, "Two"
    assert a_factaral(3) == 6, "Six"
    assert a_factaral(100) == \
           93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000, "Infinity"
