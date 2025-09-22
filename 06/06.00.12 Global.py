# If you initialize some variable inside of the function, you won't be able to use this variable outside of it.

# We receive error NameError: name 'a' is not defined. 
# Such variables declared within a function are called local. 
# They become unavailable after you exit the function. 
# To get to access to the variable 'a', you will have to return the value to the calling program. 
# To correct this problem, change print(a) to print(b).

def myFunction():
	a = "A is a local variable"
	return a
	
b = myFunction()
print(a)