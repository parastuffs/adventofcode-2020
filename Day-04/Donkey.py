def resetChecklist():
	return {'byr':False, 'iyr':False, 'eyr':False, 'hgt':False, 'hcl':False, 'ecl':False, 'pid':False}


if __name__ == "__main__":
	with open("input", 'r') as f:
		lines = f.readlines()
	lines.append("\n")

	correctPassport = 0
	isCorrect = False
	checkList = resetChecklist()
	fieldsToCheck = list(checkList.keys())

	for line in lines:
		for field in fieldsToCheck:
			if field in line:
				checkList[field] = True
		if line == "\n":
			isCorrect = True
			for value in checkList.values():
				if value == False:
					isCorrect = False
					break
			if isCorrect:
				correctPassport += 1
			checkList = resetChecklist()

	print("Valid passports: {}".format(correctPassport))
