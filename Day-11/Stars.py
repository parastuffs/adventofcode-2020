import copy

def occupied(seats, row, col):
	tot = 0
	for i in range(max(0,row-1), min(len(seats),row+2)):
		for j in range(max(0,col-1), min(len(seats[0]),col+2)):
			if i!=row or j!=col:
				if seats[i][j] == '#':
					tot += 1
	return tot

with open("input", 'r') as f:
	lines = f.readlines()
lines = [list(x.strip("\n")) for x in lines]
workplan = copy.deepcopy(lines)

stability = False
n = 0

while not stability:
	stability = True
	n += 1

	# A free seat with no occupied seat in its vicinity becomes occupied.
	lines = copy.deepcopy(workplan)
	for i, row in enumerate(lines):
		for j in range(len(row)):
			if row[j] == 'L':
				count = occupied(lines, i, j)
				if count == 0:
					workplan[i][j] = '#'
					if workplan[i][j] != lines[i][j]:
						stability = False
	lines = copy.deepcopy(workplan)

	# An occupied seat with at least 4 other occupied near becomes available.
	for i, row in enumerate(lines):
		for j in range(len(row)):
			if row[j] == '#':
				count = occupied(lines, i, j)
				if count >= 4:
					workplan[i][j] = 'L'
					if workplan[i][j] != lines[i][j]:
						stability = False

final = 0
for line in workplan:
	final += line.count('#')
print("Occupied seats: {}".format(final))