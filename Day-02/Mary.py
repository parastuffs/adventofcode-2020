with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

lowest = 0
highest = 0
checkChar = ''
correctPasswords = 0

for line in lines:
	lowest = int(line.split('-')[0])
	highest = int(line.split('-')[1].split()[0])
	checkChar = line.split('-')[1].split()[1].strip(':')
	password = line.split()[-1]
	count = password.count(checkChar)
	if count >= lowest and count <= highest:
		correctPasswords += 1
print("Correct password: {}".format(correctPasswords))