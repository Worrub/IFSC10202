import math
#Radius = input ("Enter Radius of Sphere: ")
Radius = 6371
x1_str = math.radians = input ("Enter Starting Point Longitude (x1): ")
y1_str = math.radians = input ("Enter Starting Point Latitude(y1): ")
x2_str = math.radians = input ("Enter Ending Point Longitude(x2): ")
y2_str = math.radians = input ("Enter Ending Point Latitude(y2): ")
x1 = float (x1_str)
x2 = float (x2_str)
y1 = float (y1_str)
y2 = float (y2_str)
Distance = Radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1-y2)) 
# Distance=r*arccos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
print ("The Great Circle Distance is:", Distance)