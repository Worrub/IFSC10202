height = int(input("Enter Maximum Height", ))
print("Pattern 1")
for x in range (0,height):
    for y in range (x):
        print("*", end=" ")
    print()
for x in range (height,0,-1):
    for y in range (x):
         print("*", end=" ")
    print()
##Create a program that displays the following pattern for a given height
#* 
#* * 
#* * * 
#* * * * 
#* * * 
#* * 
#* 