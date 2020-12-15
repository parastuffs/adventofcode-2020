with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]


memory = dict() # {address : value}
addresses = list()
for line in lines:
	if 'mask' in line:
		mask = line.split()[2]
	else:
		addresses = list()
		address = int(line.split('[')[1].split(']')[0])
		binary = format(address, '036b')
		maskedValue = list(binary)
		for i, bit in enumerate(binary):
			if mask[i] == 'X' or mask[i] == '1':
				maskedValue[i] = mask[i]
		addresses.append(''.join(maskedValue))
		while 'X' in addresses[0]:
			newAddresses = list()
			for address in addresses:
				a = address.replace('X', '0', 1)
				b = address.replace('X', '1', 1)
				newAddresses.append(a)
				newAddresses.append(b)
			addresses = newAddresses.copy()
		value = int(line.split()[-1])
		for address in addresses:
			memory[address] = value

print("Sum: {}".format(sum(memory.values())))