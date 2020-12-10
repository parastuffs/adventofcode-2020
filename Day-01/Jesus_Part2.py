import random

def findThem(values):
	a=b=c=0
	while a+b+c != 2020:
		a,b,c = (random.choice(values),random.choice(values),random.choice(values))
	return a,b,c


if __name__ == "__main__":

	with open("input_part2", 'r') as f:
		values = f.readlines()
	values = [x.strip("\n") for x in values]
	values = list(map(int, values))
	a,b,c = findThem(values)
	
	print("{} * {} * {} = {}".format(a, b, c, a*b*c))
