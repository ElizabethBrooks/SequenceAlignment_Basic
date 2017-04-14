# Name: Elizabeth Brooks
# File : alignPython.py
# Date: 13 April 2017

# Gain access to a file
fileIn = open("seq.txt")
# Prompt user to specify what source sequence to match
source = input("Please input source sequence: ")
# Declaration of a best sequence match variables
bestScore = 0
matchedLine = None
matchDisplacement = 0
indexMatch = 0
# Retrieve lines from the seq.txt file
for line in fileIn:
	# Score the source sequence to words in the current line, 
	# character-by-character starting after the colon
	indexLine = 0
	while indexLine <= (len(line) - len(source)) :
		tempScore = 0
		indexSource = 0
		while indexSource < len(source) :
			# Add 5 to current word placement score for matches 
			# and subtract 3 for mismatches
			indexMatch = indexLine + indexSource;
			if (line[indexMatch] == source[indexSource]) :
				tempScore = tempScore + 5;
			else:
				tempScore = tempScore - 3;
			indexSouce = indexSource + 1;
		if (tempScore >= bestScore) :
			bestScore = tempScore
			matchedLine = line
			matchDisplacement = indexLine + 1
		indexLine = indexLine + 1;
# Print the best matched line and score for the input source
print("SOURCE: " + source + "\nHighest score: " + str(bestScore) + "\nBest match line: " + matchedLine[:10] + "\n" + source.rjust(matchDisplacement) + "\n" + matchedLine)