with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]
values = list(map(int, lines))
values.append(0)
values.append(max(values)+3)

values.sort()
diff3 = 0
diff1 = 0

for i, value in enumerate(values[1:]):
	if (value - values[i]) == 1:
		diff1 += 1
	elif (value - values[i]) == 3:
		diff3 += 1

print("Product: {}".format(diff1 * diff3))