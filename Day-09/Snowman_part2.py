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

key = values[windowStart+p]

weakness = 0

for i,value in enumerate(values):
	window = [value]
	for el in values[i+1:]:
		window.append(el)
		if sum(window) > key:
			break
		elif sum(window) == key:
			weakness = min(window) + max(window)
			break
	if weakness > 0:
		break
print("Weakness: {}".format(weakness))