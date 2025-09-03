x=input("Enter Time in Seconds: ")
x=int(x)
Years = x // (365 * 24 * 60 * 60)
x = x - (Years * 365 * 24 * 60 * 60)
Days = x // (24 * 60 * 60)
x = x - Days * 24 * 60 * 60
Hours = x // (60 * 60)
x = x - Hours * 60 * 60
Minutes = x // (60)
x = x - Minutes * 60
Seconds = x
#take total, divide by seconds in years/hours/days or whatever, then subtract from total and repeat for lesser values 
print("Years", Years)
print("Days", Days)
print("Hours", Hours)
print("Minutes", Minutes)
print("Seconds", Seconds)