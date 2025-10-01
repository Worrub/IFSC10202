#Fix code only overwriting line 1 of input and only with line 1 of merge into output
#Whelp there goes all my GD'ed progress
inputfilename = "06/06.Project Input File.txt"
mergefilename = "06/06.Project Merge File.txt"
outputfilename = "06/06.Project Output File.txt"

recordcount = 0

inputfile = open(inputfilename, 'r')
line = inputfile.readline()
with open(inputfilename, 'r') as file:
    content = file.read()
    lines = content.splitlines(1)
with open(inputfilename, 'r') as file:
    content = file.read()
    lines = content.splitlines(2)
with open(inputfilename, 'r') as file:
    content = file.read()
    lines = content.splitlines(3)
with open(inputfilename, 'r') as file:
    content = file.read()
    lines = content.splitlines(4)
with open(inputfilename, 'r') as file:
    content = file.read()
    lines = content.splitlines(5)

mergefile = open(mergefilename, 'r')
line = mergefile.readline()
with open(mergefilename, 'r') as file:
    content = file.read()
    lines = content.splitlines(1)
with open(mergefilename, 'r') as file:
    content = file.read()
    lines = content.splitlines(2)           

outputfile = open(outputfilename, 'w')
for line in inputfile:1
outputfile.write(line)
for line in inputfile:2
outputfile.write(line)

for line in mergefile:1
outputfile.write(line)
for line in mergefile:2
outputfile.write(line)

for line in inputfile:4
outputfile.write(line)
for line in inputfile:5
outputfile.write(line)

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