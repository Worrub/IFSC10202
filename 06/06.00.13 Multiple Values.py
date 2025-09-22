# It is often useful for a function to return more than one value. 
# +Here's the example of returning two or more values: return a, b

def addth(m,n):
# Add 'th' to end of word
    return m + "th", n + "th"
 
a = input("Enter First Word: ")
b = input("Ender Second Word: ")
 
x, y = addth(a, b)
print(x)
print(y)