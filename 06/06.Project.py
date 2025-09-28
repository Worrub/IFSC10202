# Create a python solution that merges the contents of two files into a new file.
# Open 06.Project Output File.txt for writing
# Open and read 06.Project Input File.txt, copying lines from 06.Project Input File.txt to 06.Project Output File.txt line by line. 
# Keep a count of the number of input records and output records.
# Inspect each line of the input file for the text: **Insert Merge File Here**
# At this point, open 06.Project Merge File.txt, copying lines from 06.Project Merge File.txt to 06.Project Output File.txt line by line. 
# Keep a count of the number of merge records and output records.
# At the end of 06.Project Merge File.txt, continue copying lines from 06.Project Input File.txt to 06.Project Output File.txt line by line.
# Keep a count of the number of input records and output records.
# lose all files
# Print the number of records in the input file, merge file, and output file.
inputfilename = "06/06.Project Input File.txt"
mergefilename = "06/06.Project Merge File.txt"
outputfilename = "06/06.Project Output File.txt"

recordcount = 0

inputfile = open(inputfilename, 'r')
mergefile = open(mergefilename, 'r')
outputfile = open(outputfilename, 'w')  
# Read the first line of the input file
line = inputfile.readline()
line = mergefile.readline()

while line != '':
    
     outputfile.write(line)
     recordcount += 1
     line = inputfile.readline()

with open("06/06.Project Output File.txt", "w") as f:
    f.write("Line 1 \nLine 2")
("06/06.Project Merge File.txt", "06/06.Project Output File.txt")

inputfile.close()
mergefile.close()
outputfile.close()
print("{} records written".format(recordcount))