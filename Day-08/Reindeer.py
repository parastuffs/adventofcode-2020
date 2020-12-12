
with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

PC = 0
ACC = 0
pastPC = list()

while PC < len(lines):
	if PC in pastPC:
		break
	else:
		pastPC.append(PC)
		opcode = lines[PC].split()[0]
		mod = int(lines[PC].split()[1])
		if opcode == "nop":
			PC += 1
			continue
		elif opcode == "acc":
			PC += 1
			ACC += mod
		elif opcode == "jmp":
			PC += mod

print("Last ACC = {}".format(ACC))