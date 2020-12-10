from functools import reduce
with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

width = len(lines[0])
maxDepth = len(lines)

pos = 0 # horizontal position
depth = 0 # vertical depth
right = [1,3,5,7,1]
down = [1,1,1,1,2]
trees = [0,0,0,0,0]

for k in range(len(right)):
	pos = 0 # horizontal position
	depth = 0 # vertical depth
	# print(lines[depth])
	while depth < maxDepth-1:
		for i in range(right[k]):
			pos = (pos+1)%width
		for i in range(down[k]):
			depth += 1
		if lines[depth][pos] == '#':
			trees[k] += 1

print("Encountered {} trees, product: {}".format(trees, reduce(lambda x, y: x*y, trees)))