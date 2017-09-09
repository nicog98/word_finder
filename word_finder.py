"""
word_finder:

given an input word, find all of the words that can be 
made using its letters.
Example
INPUT:
toy
OUTPUT:
to
toy
oy
yo
"""

# Open words file
words = open("en.txt", "r")

# convert file into a set
word_list = set(line.lower().strip() for line in words)

# Find all possible letter combinations
# For each letter, find all possible letter combinations starting with that same letter
# new = start letter
# remaining = remaining letters
def word_combinations(new, remaining):
	if len(remaining) == 0 and new in word_list:
			print new
	# words with less letters than original word included
	elif new in word_list:
		print new
	for i, c in enumerate(remaining):
		# add a character from remaining characters to new combination
		comb = new + c
		# remove added character from remaining collection
		left = remaining[:i] + remaining[i+1:]
		# recurse with new combination and collection of remaining letters
		word_combinations(comb, left)

def find_words(intial):
	for i, c in enumerate(word):
		remaining = word[:i] + word[i+1:]
		word_combinations(c, remaining)

# Get word inputs until user defers
word = raw_input("Word: (Enter to quit) ")
while word is not "":
	find_words(word)
	word = raw_input("Word: ")
print "Exiting... Thank you!"