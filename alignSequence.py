# Name: Elizabeth Brooks
# File : alignPython.py
# Date: 14 April 2017

# Gain access to a file
fileIn = open("seq.txt")
# Prompt user to specify what source sequence to match
source = input("Please input source sequence: ")
# Declaration of variables to track the highest scoring source/sequence match
bestScore = 0
matchedLine = None
matchDisplacement = 0
indexMatch = 0
# Retrieve lines from the seq.txt file
for line in fileIn:
	# Score the source sequence to words in the current line, 
	# character-by-character starting after the colon
	indexLine = 0
	# Traverese the line sequence by character
	while indexLine <= (len(line) - len(source)) :
		# Make sure to only check the sequence in the line, after the id
		if (indexLine >= 10) :
			tempScore = 0
			indexSource = 0
			# Traverse the characters of the source word and current line segment
			while indexSource < len(source) :
				# Move line index with word index by character
				indexMatch = indexLine + indexSource
				# Add 5 to current word placement score for matches
				# and subtract 3 for mismatches
				if (line[indexMatch] == source[indexSource]) :
					tempScore = tempScore + 5
				else:
					tempScore = tempScore - 3
				# Move the word index by charcter
				indexSource = indexSource + 1
			# Keep track of the last highest score, line, and placememnt
			if (tempScore >= bestScore) :
				bestScore = tempScore
				matchedLine = line
				matchDisplacement = indexLine
		# Move the line index by character
		indexLine = indexLine + 1
# Print the best matched line and score for the input source
# as well as the source sequence and last found matched sequence
print("\nSOURCE: " + source + "\nHighest score: " + str(bestScore) + "\nLast best match: " + matchedLine[:8] + "\n\n" + source.rjust(matchDisplacement) + "\n" + ('|'*len(source)).rjust(matchDisplacement) + "\n" + matchedLine[10:])
