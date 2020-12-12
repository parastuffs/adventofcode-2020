

with open("input", 'r') as f:
	lines = f.readlines()
# lines = [x.strip("\n") for x in lines]
lines.append("\n")

total = 0

answers = set()
for line in lines:
	if line == "\n":
		total += len(answers)
		answers = set()
	else:
		for letter in line.strip("\n"):
			answers.add(letter)

print("Total: {}".format(total))
