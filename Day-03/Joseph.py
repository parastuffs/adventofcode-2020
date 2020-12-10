with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

width = len(lines[0])
maxDepth = len(lines)

# landscape = list()
# for line in lines:
# 	landscape.extend(line)

pos = 0 # horizontal position
depth = 0 # vertical depth
right = 3
down = 1
trees = 0

# print(lines[depth])
while depth < maxDepth-1:
	for i in range(right):
		pos = (pos+1)%width
		# if pos == width:
		# 	pos = 0
			# depth += 1
		# print("Checking line {} pos {}".format(depth, pos))
		# if lines[depth][pos] == '#':
		# 	trees += 1
			# print("Tree!")
	for i in range(down):
		depth += 1
		# print(lines[depth])
		if lines[depth][pos] == '#':
			trees += 1
			# print("Tree!")

print("Encountered {} trees".format(trees))