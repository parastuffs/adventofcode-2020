import re
def resetChecklist():
	return {'byr':False, 'iyr':False, 'eyr':False, 'hgt':False, 'hcl':False, 'ecl':False, 'pid':False}


if __name__ == "__main__":
	with open("input", 'r') as f:
		lines = f.readlines()
	# lines = [x.strip("\n") for x in lines]
	lines.append("\n")

	correctPassport = 0
	isCorrect = False
	checkList = resetChecklist()
	fieldsToCheck = list(checkList.keys())

	for line in lines:
		if line == "\n":
			isCorrect = True
			for value in checkList.values():
				if value == False:
					isCorrect = False
					break
			if isCorrect:
				correctPassport += 1
			checkList = resetChecklist()
		else:
			line = line.strip("\n")
			for el in line.split():
				tag,value = el.split(':')

				if tag == "byr":
					value = int(value)
					if value >= 1920 and value <= 2002:
						checkList[tag] = True
				elif tag == "iyr":
					value = int(value)
					if value >= 2010 and value <= 2020:
						checkList[tag] = True
				elif tag == "eyr":
					value = int(value)
					if value >= 2020 and value <= 2030:
						checkList[tag] = True
				elif tag == "hgt":
					if 'cm' in value:
						value = value.replace('cm', '')
						value = int(value)
						if value >= 150 and value <= 193:
							checkList[tag] = True
					elif 'in' in value:
						value = value.replace('in', '')
						value = int(value)
						if value >= 59 and value <= 76:
							checkList[tag] = True
				elif tag == "hcl":
					p = re.compile('^#[0-9a-f]{6}$')
					if p.match(value):
						checkList[tag] = True
				elif tag == "ecl":
					eyeColors = ['amb','blu','brn','gry','grn','hzl','oth']
					if value in eyeColors:
						checkList[tag] = True
				elif tag == "pid":
					p = re.compile('^[0-9]{9}$')
					if p.match(value):
						checkList[tag] = True

	print("Valid passports: {}".format(correctPassport))
