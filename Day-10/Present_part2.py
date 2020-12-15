chain = dict()

def findNextJolt(index, adapters):
	tot = 0
	if index == len(adapters)-1:
		return 1
	if index in chain: # If we already encountered this point in the tree, return the value we recorded.
		return chain[index]
	for i in range(index+1, len(adapters)):
		if adapters[i] - adapters[index] <= 3:
			tot += findNextJolt(i, adapters)
	chain[index] = tot # Remember the value from this point on.
	return tot


with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]
values = list(map(int, lines))
values.append(0)
values.append(max(values)+3)

values.sort()

print(values)
final = findNextJolt(0, values)
print(final)
