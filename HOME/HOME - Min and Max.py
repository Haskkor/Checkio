##In this mission you should write you own py3 implementation (but you can use py2 for this) of the built-in functions min and max. Some builtin functions are closed here: import, eval, exec, globals. Don't forget you should implement two functions in your code.
##
##max(iterable, *[, key]) or min(iterable, *[, key])
##max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])
##
##Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.
##
##If one positional argument is provided, it should be an iterable. The largest (smallest) item in the iterable is returned. If two or more positional arguments are provided, the largest (smallest) of the positional arguments is returned.
##
##The optional keyword-only key argument specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower).
##
##If multiple items are maximal (minimal), the function returns the first one encountered.
##
##-- Python Documentation (Built-in Functions)
##
##Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.
##
##Output: The largest item for the "max" function and the smallest for the "min" function.
##
##Example:
##
##max(3, 2) == 3
##min(3, 2) == 2
##max([1, 2, 0, 3, 4]) == 4
##min("hello") == "e"
##max(2.2, 5.6, 5.9, key=int) == 5.6
##min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
##    
##How it is used: This task will help you understand how some of the built-in functions work on a more precise level.
##
##Precondition: All test cases are correct and functions don't have to raise exceptions.

import types

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if key == None:
        key = lambda x: x
    try:
        min = args[0][0]
        for elem in args:
            for el in elem:
                if key(el) < key(min) and isinstance(elem, list):
                    min = elem
                elif key(el) < min:
                    min = el       
    except:
        if isinstance(args[0], types.GeneratorType):
            args = list(args[0])
            min = key(args[0])
        else:
            if len(args) == 1:
                args = list(args[0])
            min = args[0]
        for elem in args:
            if key(elem) < key(min):
                min = elem
    return min

def max(*args, **kwargs):
    key = kwargs.get("key", None)
        
    if key == None:
        key = lambda x: x
            
    try:
        max = key(args[0][0])
        for elem in args:
            for el in elem:
                if key(el) > max and isinstance(elem, list):
                    max = elem
                else:
                    max = el       
    except:
        if isinstance(args[0], types.GeneratorType):
            args = list(args[0])
            max = key(args[0])
        else:
            if len(args) == 1:
                args = list(args[0])
            max = key(args[0])
        for elem in args:
            if key(elem) > max:
                max = elem
    return max


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min((9,)) == 9
    assert min(abs(i) for i in range(-10, 10)) == 0
    assert max(x + 5 for x in range(6)) == 10
    assert max(filter(str.isalpha,"@v$e56r5CY{]")) == "v"
    assert max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]) == [7]
    assert min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum) == [1,2,3]
