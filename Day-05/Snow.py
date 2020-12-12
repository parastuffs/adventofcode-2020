def findRow(code, rows):
	'''
	Code : Str sequence such as FFBFFBB
	rows : list [O...n]
	'''
	if len(code)>1:
		if code[0] == 'F':
			return findRow(code[1:], rows[0:int(len(rows)/2)])
		elif code[0] == 'B':
			return findRow(code[1:], rows[int((len(rows)/2)):])
		else:
			print("Unexpected row instruction: '{}'".format(code[0]))
	else:
		if code[0] == 'F':
			return rows[0]
		elif code[0] == 'B':
			return rows[-1]
		else:
			print("Unexpected row instruction: '{}'".format(code[0]))

def findColumn(code, columns):
	'''
	Code : Str sequence such as FFBFFBB
	columns : list [O...n]
	'''
	if len(code)>1:
		if code[0] == 'L':
			return findColumn(code[1:], columns[0:int(len(columns)/2)])
		elif code[0] == 'R':
			return findColumn(code[1:], columns[int((len(columns)/2)):])
		else:
			print("Unexpected column instruction: '{}'".format(code[0]))
	else:
		if code[0] == 'L':
			return columns[0]
		elif code[0] == 'R':
			return columns[-1]
		else:
			print("Unexpected column instruction: '{}'".format(code[0]))


with open("input", 'r') as f:
	lines = f.readlines()
lines = [x.strip("\n") for x in lines]
rows = [x for x in range(128)]
columns = [x for x in range(8)]
ids = list()

for line in lines:
	# line[0:7] => row
	# lines[7:9] => column
	row = findRow(line[0:7], rows)
	col = findColumn(line[7:], columns)
	ids.append(row * 8 + col)
print("Max ID: {}".format(max(ids)))