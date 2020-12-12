def dbg(code, start):
	i=0
	for i, line in enumerate(code[start:]):
		if 'jmp' in line:
			code[i+start] = line.replace('jmp','nop')
			break
		elif 'nop' in line:
			code[i+start] = line.replace('nop', 'jmp')
			break
	return code, i+start

with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

PC = 0
ACC = 0
pastPC = list()
lastChange = 0

resolved = False

code = lines.copy()

while not resolved:
	PC = 0
	ACC = 0
	pastPC = list()
	infiniteLoop = False

	while PC < len(code):
		if PC in pastPC:
			infiniteLoop = True
			break
		else:
			pastPC.append(PC)
			opcode = code[PC].split()[0]
			mod = int(code[PC].split()[1])
			if opcode == "nop":
				PC += 1
				continue
			elif opcode == "acc":
				PC += 1
				ACC += mod
			elif opcode == "jmp":
				PC += mod

	if infiniteLoop:
		code, lastChange = dbg(lines.copy(), lastChange+1)
	else:
		resolved = True

print("Last ACC = {}".format(ACC))