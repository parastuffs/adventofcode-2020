with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]


memory = dict() # {address : value}
for line in lines:
	if 'mask' in line:
		mask = lines[0].split()[2]
	else:
		address = line.split('[')[1].split(']')[0]
		value = int(line.split()[-1])
		binary = format(value, '036b')
		maskedValue = list(binary)
		for i, bit in enumerate(reversed(binary)):
			if mask[-(i+1)] != 'X':
				maskedValue[-(i+1)] = mask[-(i+1)]
		final = int(''.join(maskedValue), 2)
		memory[address] = final

print("Sum: {}".format(sum(memory.values())))