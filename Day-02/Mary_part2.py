with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

lowest = 0
highest = 0
checkChar = ''
correctPasswords = 0

for line in lines:
	found = False
	lowest = int(line.split('-')[0])-1
	highest = int(line.split('-')[1].split()[0])-1
	checkChar = line.split('-')[1].split()[1].strip(':')
	password = line.split()[-1]
	if password[lowest] == checkChar:
		found = True
	if password[highest] == checkChar:
		found = not found
	if found:
		correctPasswords += 1
		print("Correct: {}".format(line))
print("Correct password: {}".format(correctPasswords))