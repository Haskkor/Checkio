##Two functions f and g are provided as inputs to checkio. The first function f is the primary function and the second function g is the backup. Use your coding skills to return a third function h which returns the same output as f unless f raises an exception or returns None. In this case h should return the same output as g. If both f and g raise exceptions or return None, then h should return None.
##
##As a second output, h should return a status string indicating whether the function values are the same and if either function erred. A function errs if it raises an exception or returns a null value (None).
##
##The status string should be set to: "same" if f and g return the same output and neither errs, "different" if f and g return different outputs and neither errs, "f_error" if f errs but not g, "g_error" if g errs but not f, or "both_error" if both err.
##
##Input: Two functions: f (primary) and g (backup).
##
##Output: A function h which takes arbitrary inputs and returns a two-tuple.
##
##Example:
##
##        f = lambda x,y: x+y
##        g = lambda x,y: (x**2 - y**2)/(x-y)
##        checkio(f,g)(1,3) == (4,"same")
##        checkio(f,g)(1,1.01) == (2.01,"different") # numerical precision difference
##        checkio(f,g)(1,1) == (2,"g_error") # g divides by zero
##
##How it is used: This is an exercise in working with functions as first class objects.
##
##Precondition: hasattr(f,'__call__');
##hasattr(g,'__call__')

def checkio(f,g):
    def h(*args,**kwargs):
        try:
            f_res = f(*args,**kwargs)
        except:
            try:g_res = g(*args,**kwargs)
            except:return (None,'both_error')
            else:
                if g_res != None:return (g_res,'f_error')
                else:return (None,'both_error')
        else:
            try:g_res = g(*args,**kwargs)
            except:return (f_res,'g_error')
            else:
                if f_res == None and g_res != None:return (g_res,'f_error')
                elif f_res != None and g_res == None:return (f_res,'g_error')
                elif f_res == None and g_res == None:return (None,'both_error')
                elif f_res == g_res:return (f_res,'same')
                else:return (f_res,'different')
    return h

if __name__ == '__main__':
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    # (x+y)(x-y)/(x-y)
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,3)==(4,'same'), "Function: x+y, first"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,2)==(3,'same'), "Function: x+y, second"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01)==(2.01,'different'), "x+y, third"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1)==(2,'g_error'), "x+y, fourth"
                   
    # Remove odds from list               
    f = lambda nums:[x for x in nums if ~x%2]
    def g(nums):
      for i in range(len(nums)):
        if nums[i]%2==1:
          nums.pop(i)
      return nums 
    assert checkio(f,g)([2,4,6,8]) == ([2,4,6,8],'same'), "evens, first"
    assert checkio(f,g)([2,3,4,6,8]) == ([2,4,6,8],'g_error'), "evens, second"         
    
    # Fizz Buzz    
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (6)==('Fizz','same'), "fizz buzz, first"      
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (30)==('Fizz Buzz','same'), "fizz buzz, second"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (7)==('7','different'), "fizz buzz, third"
