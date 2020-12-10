def findThem(values):
	a = b = 0
	for i,value in enumerate(values):
		a = value
		for subvalue in values[i+1:]:
			b = subvalue
			if (a+b) == 2020:
				return a,b


if __name__ == "__main__":

	with open("input", 'r') as f:
		values = f.readlines()
	values = [x.strip("\n") for x in values]
	values = list(map(int, values))
	a,b = findThem(values)
	
	print("{} * {} = {}".format(a, b, a*b))
