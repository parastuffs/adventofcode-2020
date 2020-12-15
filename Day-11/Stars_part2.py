import copy

def occupied(seats, row, col):
	tot = 0
	# print(seats)
	# print("{}, {}".format(row, col))
	# N
	for i in reversed(range(0, row)):
		if seats[i][col] == '#':
			tot += 1
			# print("Seat in N, {}".format(i))
			break
		elif seats[i][col] == 'L':
			break
	# S
	for i in range(row+1, len(seats)):
		if seats[i][col] == '#':
			tot += 1
			# print("Seat in S, {}".format(i))
			break
		elif seats[i][col] == 'L':
			break
	# W
	for i in reversed(range(0, col)):
		if seats[row][i] == '#':
			tot += 1
			# print("Seat in W, {}".format(i))
			break
		elif seats[row][i] == 'L':
			break
	# E
	for i in range(col+1, len(seats[0])):
		if seats[row][i] == '#':
			tot += 1
			# print("Seat in E, {}".format(i))
			break
		elif seats[row][i] == 'L':
			break
	# NW
	i = row-1
	j = col-1
	while i>=0 and j>=0:
		if seats[i][j] == '#':
			tot += 1
			# print("Seat in NW, {},{}".format(i,j))
			break
		elif seats[i][j] == 'L':
			break
		i -= 1
		j -= 1
	# NE
	i = row-1
	j = col+1
	while i>=0 and j<len(seats[0]):
		if seats[i][j] == '#':
			tot += 1
			# print("Seat in NE, {},{}".format(i,j))
			break
		elif seats[i][j] == 'L':
			break
		i -= 1
		j += 1
	# SE
	i = row+1
	j = col+1
	while i<len(seats) and j<len(seats[0]):
		if seats[i][j] == '#':
			tot += 1
			# print("Seat in SE, {},{}".format(i,j))
			break
		elif seats[i][j] == 'L':
			break
		i += 1
		j += 1
	# SW
	i = row+1
	j = col-1
	while i<len(seats) and j>=0:
		if seats[i][j] == '#':
			tot += 1
			# print("Seat in SW, {},{}".format(i,j))
			break
		elif seats[i][j] == 'L':
			break
		i += 1
		j -= 1
	return tot


with open("input", 'r') as f:
	lines = f.readlines()
lines = [list(x.strip("\n")) for x in lines]
workplan = copy.deepcopy(lines)

stability = False
n = 0

while (not stability):
	stability = True
	n += 1
	# print("Run {}".format(n))

	# A free seat with no occupied seat in its vicinity becomes occupied.
	lines = copy.deepcopy(workplan)
	for i, row in enumerate(lines):
		# print(lines)
		for j in range(len(row)):
			if row[j] == 'L':
				count = occupied(lines, i, j)
				if count == 0:
					workplan[i][j] = '#'
					if workplan[i][j] != lines[i][j]:
						stability = False
			# break
		# break
	lines = copy.deepcopy(workplan)

	# for line in workplan:
	# 	print(''.join(line))
	# print("-----------------------")

	# An occupied seat with at least 4 other occupied near becomes available.
	for i, row in enumerate(lines):
		for j in range(len(row)):
			if row[j] == '#':
				count = occupied(lines, i, j)
				# print("i: {}, j: {}, count:{}".format(i,j,count))
				if count >= 5:
					workplan[i][j] = 'L'
					if workplan[i][j] != lines[i][j]:
						stability = False
	lines = workplan.copy()
	# for line in workplan:
	# 	print(''.join(line))
	# print("-----------------------")

final = 0
for line in workplan:
	final += line.count('#')
print("Occupied seats: {}".format(final))