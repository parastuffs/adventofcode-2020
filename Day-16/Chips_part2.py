with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

fields = dict()

# for line in lines[0:3]: #input_test.1
for line in lines[0:20]: #input
# for line in lines[0:3]: #input_test.2
	print(line)
	fields[line.split(':')[0]] = [int(line.split(': ')[1].split(' or ')[0].split('-')[0]),
	int(line.split(': ')[1].split(' or ')[0].split('-')[1]),int(line.split(': ')[1].split(' or ')[1].split('-')[0]),int(line.split(': ')[1].split(' or ')[1].split('-')[1])]
print(fields)

# myTicket = lines[5].split(',') #input_test.1
myTicket = lines[22].split(',') #input
# myTicket = lines[5].split(',') #input_test.2
myTicket = list(map(int,myTicket))

total = 0
validTickets = list()


#####################################
# List all valid tickets
#####################################

# for line in lines[8:]: #input_test.1
for line in lines[26:]: #input
# for line in lines[8:]: #input_test.2
	ticketIsValid = True
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
			ticketIsValid = False
			total += value
			break
	if ticketIsValid:
		# print("Valid ticket")
		validTickets.append(list(map(int,line.split(','))))


#############################################
# List translation canditates for each field
#############################################

translation = dict() # {index : field}
IDs = [x for x in range(len(fields))] # All possible IDs not assigned yet.
candidates = dict() # {field : [candidates]}

for field in fields.keys():
	# print("Translating '{}'".format(field))
	candidates[field] = list()
	for i in IDs:
		valid = False
		for ticket in validTickets:
			value = ticket[i]
			values = fields[field]
			if (value >= values[0] and value <= values[1]) or (value >= values[2] and value <= values[3]):
					valid = True
			else:
				valid = False
				break
		if valid:
			candidates[field].append(i)


#####################################################
# Take the next field with the least candidates and 
# assign it an ID not yet taken.
#####################################################

print(candidates)
i = 1
takenIDs = list() # list of IDs assigned to a field.
while i < len(fields):
	for field in candidates:
		if len(candidates[field]) == i:
			for value in candidates[field]:
				if value not in takenIDs:
					translation[field] = value
					takenIDs.append(value)
					break

	i += 1

print(translation)


#######################################
# Find the desired fields in my ticket
#######################################

product = 1
for idx, value in enumerate(myTicket):
	print("Looking for {}".format(value))
	for field in translation:
		if translation[field] == idx and 'departure' in field:
			product *= value

print("Product: {}".format(product))

