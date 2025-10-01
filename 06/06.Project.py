#Fix code only overwriting line 1 of input and only with line 1 of merge into output
#Whelp there goes all my GD progress
inputfilename = "06/06.Project Input File.txt"
mergefilename = "06/06.Project Merge File.txt"
outputfilename = "06/06.Project Output File.txt"

recordcount = 0

inputfile = open(inputfilename, 'r')
line = inputfile.readline()

mergefile = open(mergefilename, 'r')
line = mergefile.readline()

outputfile = open(outputfilename, 'w')
for line in inputfile:1
for line in inputfile:2
for line in inputfile:3

for line in mergefile:1
for line in mergefile:2

for line in inputfile:4
for line in inputfile:5

while line != '':
    
     outputfile.write(line)
     recordcount += 1
     line = inputfile.readline()

with open ("06/06.Project Output File.txt", "w") as f:
    f.write("Line 1\nLine 2")
    ("06/06.Project Merge File.txt", "06/06.Project Output File.txt")


inputfile.close()
mergefile.close()
outputfile.close()
print("{} records written".format(recordcount))