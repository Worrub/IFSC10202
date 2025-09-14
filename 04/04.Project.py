n = int(input("Enter Maximum Height", ))
print("Pattern 1")
for a1 in range (0,n):
    for a2 in range (a1):
        print("* ", end="")
    print()
for a1 in range (n,0,-1):
    for a2 in range (a1):
        print("* ", end="")
    print()
##Create a program that displays the following pattern for a given height
##Hint: Practice for this assignment by completing the 04.07 Ladder exercise
#Enter maximum height: 4
#* 
#* * 
#* * * 
#* * * * 
#* * * 
#* * 
#* 