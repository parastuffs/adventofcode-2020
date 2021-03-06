import copy

def neigbourgs(cubes, el):
	tot = 0
	z = el[0]
	y = el[1]
	x = el[2]
	# print("{}:{}".format(el,cubes[z][y][x]))
	# print(cubes)
	for i in range( max(0,z-1), min(z+2,len(cubes)) ):
		for j in range( max(0,y-1), min(y+2,len(cubes[0])) ):
			for k in range( max(0,x-1), min(x+2,len(cubes[0])) ):
				if not(i==z and j==y and k==x):
					# print("{} {} {}".format(i,j,k))
					if cubes[i][j][k] == '#':
						tot += 1
	return tot

with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]


ncubes = 6+6+1
nelements = 6+6+len(lines[0])

cubes = [[[ '.' for k in range(nelements)] for j in range(nelements)] for i in range(ncubes)]


for i in range(6,6+len(lines[0])):
	for j in range(6,6+len(lines[0])):
		cubes[6][i][j] = lines[i-6][j-6]
# print(cubes)
workingCubes = copy.deepcopy(cubes)

for run in range(6):
	for z in range(ncubes):
		for y in range(nelements):
			for x in range(nelements):
				neigh = neigbourgs(cubes, [z,y,x])
				print(neigh)
				if cubes[z][y][x] == '#':
					if neigh != 2 and neigh != 3:
						workingCubes[z][y][x] = '.'
				elif cubes[z][y][x] == '.':
					if neigh == 3:
						workingCubes[z][y][x] = '#'
	cubes = copy.deepcopy(workingCubes)

active = 0
for z in range(ncubes):
	for y in range(nelements):
		for x in range(nelements):
			if cubes[z][y][x] == '#':
				active += 1
# print(cubes)
print("Active: {}".format(active))