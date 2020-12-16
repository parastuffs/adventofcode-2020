with open("input_test.1", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

fields = dict()

for line in lines[0:3]: #input_test.1
# for line in lines[0:20]: #input
	print(line)
	fields[line.split(':')[0]] = [int(line.split(': ')[1].split(' or ')[0].split('-')[0]),
	int(line.split(': ')[1].split(' or ')[0].split('-')[1]),int(line.split(': ')[1].split(' or ')[1].split('-')[0]),int(line.split(': ')[1].split(' or ')[1].split('-')[1])]
print(fields)

ticket = lines[5].split(',') #input_test.1
# ticket = lines[22].split(',') #input
ticket = list(map(int,ticket))

total = 0

for line in lines[8:]: #input_test.1
# for line in lines[26:]: #input
	for value in line.split(','):
		found = False
		value = int(value)
		for field in fields:
			values = fields[field]
			if (value >= values[0] and value <= values[1]) or (value >= values[2] and value <= values[3]):
				found = True
				break
		if not found:
			# print("{} was not found in line {}".format(value, line))
			total += value
print("Total: {}".format(total))