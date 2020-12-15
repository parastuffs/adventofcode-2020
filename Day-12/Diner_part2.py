with open("input", 'r') as f:
	lines = f.readlines()
lines = [list(x.strip("\n")) for x in lines]


pos = [0,0] # NE is > 0
waypointPos = [10,1]
for line in lines:
	# print(line)
	order = line[0]
	value = int(''.join(line[1:]))
	if order == 'N':
		waypointPos[1] += value
	elif order == 'S':
		waypointPos[1] -= value
	elif order == 'E':
		waypointPos[0] += value
	elif order == 'W':
		waypointPos[0] -= value
	elif order == 'F':
		pos = [waypointPos[0]*value + pos[0], waypointPos[1]*value + pos[1]]
	elif order == 'R':
		if value == 90:
			waypointPos = [waypointPos[1], -waypointPos[0]]
		elif value == 180:
			waypointPos = [-waypointPos[0], -waypointPos[1]]
		elif value == 270:
			waypointPos = [-waypointPos[1], waypointPos[0]]
	elif order == 'L':
		value = (360-value)
		if value == 90:
			waypointPos = [waypointPos[1], -waypointPos[0]]
		elif value == 180:
			waypointPos = [-waypointPos[0], -waypointPos[1]]
		elif value == 270:
			waypointPos = [-waypointPos[1], waypointPos[0]]
	# print("New pos: {}, wp: {}".format(pos, waypointPos))
print("Distance: {}".format(abs(pos[0]) + abs(pos[1])))