
class Bag:
	def __init__(self, name):
		self.name = name
		self.subbags = dict() # {bage name : amount}


def canContainShiny(bag, bags):
	if "shiny gold" in bag.subbags.keys():
		return True
	elif len(bag.subbags) == 0:
		return False
	else:
		status = False
		for subbag in bag.subbags.keys():
			status = status or canContainShiny(bags[subbag], bags)
		return status


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
			# print(subbag.split()[0])
			subbagamount = int(subbag.split()[0])
			subbagname = " ".join(subbag.split()[1:3])
			bag.subbags[subbagname] = subbagamount
	bags[bagname] = bag

total = 0
for bag in bags.values():
	# shiny gold
	if canContainShiny(bag, bags):
		total += 1

print("{} bags can hold shiny gold bags.".format(total))