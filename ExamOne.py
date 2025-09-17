from random import randint
print("This game is Winners and Losers")
print("Round 1")
Human_Score = 0
Computer_Score = 0
print("Score: ","You", Human_Score, "Comp", Computer_Score)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = sum(my_list)

x_str = input("Enter Your Number (1-5): ")
y_str = randint(1, 5)
x = int(x_str)
y = int(y_str)
print("Computer's Number: ",y)
if sum % 2 == 0:
    print(f"Even! You get a Point!")
    Human_Score += 1
else:
    print(f"Odd! Computer gets a Point!")
    Computer_Score += 1
print("Score: ","You", Human_Score, "Comp", Computer_Score)

print("Round 2")
x_str = input("Enter Your Number (1-5): ")
y_str = randint(1, 5)
x = int(x_str)
y = int(y_str)
print("Computer's Number: ",y)
if sum % 2 == 0:
    print(f"Even! You get a Point!")
    Human_Score += 1
else:
    print(f"Odd! Computer gets a Point!")
    Computer_Score += 1
print("Score: ","You", Human_Score, "Comp", Computer_Score)

print("Round 3")
x_str = input("Enter Your Number (1-5): ")
y_str = randint(1, 5)
x = int(x_str)
y = int(y_str)
print("Computer's Number: ",y)
if sum % 2 == 0:
    print(f"Even! You get a Point!")
    Human_Score += 1
else:
    print(f"Odd! Computer gets a Point!")
    Computer_Score += 1
print("Score: ","You", Human_Score, "Comp", Computer_Score)

print("Round 4")
x_str = input("Enter Your Number (1-5): ")
y_str = randint(1, 5)
x = int(x_str)
y = int(y_str)
print("Computer's Number: ",y)
if sum % 2 == 0:
    print(f"Even! You get a Point!")
    Human_Score += 1
else:
    print(f"Odd! Computer gets a Point!")
    Computer_Score += 1
print("Score: ","You", Human_Score, "Comp", Computer_Score)

print("Final Round")
x_str = input("Enter Your Number (1-5): ")
y_str = randint(1, 5)
x = int(x_str)
y = int(y_str)
print("Computer's Number: ",y)
if sum % 2 == 0:
    print(f"Even! You get a Point!")
    Human_Score += 1
else:
    print(f"Odd! Computer gets a Point!")
    Computer_Score += 1


print("Score: ","You", Human_Score, "Comp", Computer_Score)

if Human_Score > Computer_Score:
    print("You Win!")
else:
    print("Computer Wins!")

#Human is Even, Computer is Odd
#RNG 1-5 for 5 rounds, sum of numbers given determines score
