with open("input", 'r') as f:
	lines = f.readlines()
lines = [list(x.strip("\n")) for x in lines]


pos = [0,0] # NE is > 0
facing = 0 # 0:E, 1:S, 2:W, 3:N
for line in lines:
	# print(line)
	order = line[0]
	value = int(''.join(line[1:]))
	if order == 'N':
		pos[0] += value
	elif order == 'S':
		pos[0] -= value
	elif order == 'E':
		pos[1] += value
	elif order == 'W':
		pos[1] -= value
	elif order == 'F':
		if facing == 0:
			pos[1] += value
		if facing == 1:
			pos[0] -= value
		if facing == 2:
			pos[1] -= value
		if facing == 3:
			pos[0] += value
	elif order == 'R':
		value = value/90
		facing = (facing+value)%4
	elif order == 'L':
		value = (360-value)/90
		facing = (facing+value)%4
	# print("New pos: {}".format(pos))
print("Distance: {}".format(abs(pos[0]) + abs(pos[1])))