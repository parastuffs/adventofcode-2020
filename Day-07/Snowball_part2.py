
class Bag:
	def __init__(self, name):
		self.name = name
		self.subbags = dict() # {bage name : amount}

def bagCapacity(bag, bags, total):
	subtotal = 0
	for subbag in bag.subbags.keys():
		subtotal += bag.subbags[subbag] * (bagCapacity(bags[subbag], bags, total) + 1)
	if len(bag.subbags) == 0:
		total = 0
	total += subtotal
	return total

with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]

bags = dict() # {bag name : Bag object}

# Typical line: dim olive bags contain 2 dull silver bags, 4 posh blue bags.
for line in lines:
	bagname = line.split("bags contain")[0].strip()
	bag = Bag(bagname)
	if not "contain no other bags." in line:
		for subbag in line.split("contain")[1].split(','):
			subbagamount = int(subbag.split()[0])
			subbagname = " ".join(subbag.split()[1:3])
			bag.subbags[subbagname] = subbagamount
	bags[bagname] = bag

total = 0

total = bagCapacity(bags["shiny gold"], bags, total)

print("A shiny glod bag must contain {} bags.".format(total))