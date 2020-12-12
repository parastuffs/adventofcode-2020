def checkValidity(window, value):
	for i,k in enumerate(window):
		for j in window[i+1:]:
			if (k+j) == value:
				return True
	return False

with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]
values = list(map(int, lines))

p = 25 # preamble
windowStart = -1

foundError = False
while not foundError:
	windowStart += 1
	window = values[windowStart:windowStart+p]
	foundError = not checkValidity(window, values[windowStart+p])

print("Erroneous value: {}".format(values[windowStart+p]))
