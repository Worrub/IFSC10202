# We want to provide a few explanations. 
# First, the function code should be placed in the beginning of the program (before the place where we want to use the function factorial(), to be precise). 
# The first line def factorial(n): of this example is a description of our function; the word factorial is an identifier (the name of our function). 
# Right after the identifier, there goes the list of parameters that our function receives (in parentheses). 
# The list consists of comma-separated identifiers of the parameters; in our case, there's only one parameter n. At the end of this line, put colon.

# Then goes the function body. 
# In Python, the body must be indented (by Tab or four spaces, as always). 
# This function calculates the value of n! and stores it in the variable res (meaning "result"). 
# The last line of the function is return res, which exits the function and returns the value of the variable res.

# The return statement can appear in any place of a function. 
# Its execution exits the function and returns specified value to the place where the function was called. 
# If the function does not return a value, the return statement won't actually return some value (though it still can be used). 
# Some functions do not need to return values, and the return statement can be omitted for them.

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
 
print(factorial(3))
print(factorial(5))