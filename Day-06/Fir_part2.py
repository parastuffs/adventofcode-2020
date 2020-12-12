

with open("input", 'r') as f:
	lines = f.readlines()
# lines = [x.strip("\n") for x in lines]
lines.append("\n")

total = 0

answers = None
for line in lines:
	tmpSet = set()
	if line == "\n":
		total += len(answers)
		answers = None
	else:
		for letter in line.strip("\n"):
			tmpSet.add(letter)
		if answers == None:
			answers = tmpSet.copy()
		else:
			answers = answers & tmpSet

print("Total: {}".format(total))
