
def Question():
	fname = ''
	fname = input(' (make) >> First name: ')
	while len(fname) < 3:
		fname = input(' (make) >> Needed first name: ')
	lname = input(' (make) >> Last name: ')
	nname = input(' (make) >> Nickname: ')
	birth = input(' (make) >> Birthday(mmddyyyy): ').strip()
	digits = input(' (make) >> Would you like to add number in every last word?(y/n): ').lower()
	n = 0
	if digits == 'y':
		n = int(input(' (make) >> Digit number: '))
	filename = input(' (make) >> Filename: ') + '.txt'
	return fname, lname, nname, birth, filename, digits, n

def birth_slice(birth):
	day = birth[0:2]
	month = birth[2:4]
	year = birth [4:]
	return day, month, year		# returns list together named birthday

def birth_process(day, month, year):
	dy = day + year
	yd = year + day
	my = month + year
	ym = year + month
	dm = day + month
	md = month + day
	return dy, yd, my, ym, dm, md 	# returns list birthday

def names_process(fname, lname, nname):
	fnames = [fname.upper(), fname.lower(), fname.capitalize()]
	lnames = [lname.upper(), lname.lower(), lname.capitalize()]
	nnames = [nname.upper(), nname.lower(), nname.capitalize()]
	return fnames, lnames, nnames

def combinations(fname, lname, nname, birthday, filename):
	for fname1 in fname:
		with open(filename, 'a') as f:			
				f.write(fname1 + '\n')		# firstname						
		for lname1 in lname:
			if lname1 == '' and ' ' and '  ':
				break
			else:
				with open(filename, 'a') as f:											
					f.write(fname1 + lname1 + '\n')	# firstname plus lastname	
				for birth in birthday:
					if birth == '' and ' ' and '  ':
						pass
					else:
						with open(filename, 'a') as f:
							f.write(fname1 + lname1 + birth + '\n')	# firstname plus lastname plus birthday
		for nname1 in nname:
			if nname1 == '' and ' ' and '  ':
				break
			else:
				with open(filename, 'a') as f:
					f.write(fname1 + nname1 + '\n')			# firstname plus nickname 	
				for birth in birthday:
					if birth == '' and ' ' and '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(fname1 + nname1 + birth + '\n') # firstname plus lastname plus birthday
		for birth in birthday:
			if birth == '' and ' ' and '  ':
				pass
			else:
				with open(filename, 'a') as f:
					f.write(fname1 + birth + '\n')	
					f.write(birth + fname1 + '\n')		# firstname plus birthday vice-versa
			

	for nname1 in nname:
		if nname1 == '' and ' ' and '  ':
			break
		else:						
			with open(filename, 'a') as f:			
				f.write(nname1 + '\n')	# nickname
			for lname1 in lname:
				if lname1 == '' and ' ' and '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1 + lname1 + '\n')	# nickname plus lastname
					for birth in birthday:
						if birth == '' and ' ' and '  ':
							break
						else:
							with open(filename, 'a') as f:
								f.write(nname1 + lname1 + birth + '\n')	# nickname plus lastname plus birthday
			for fname1 in fname:
				with open(filename, 'a') as f:
					f.write(nname1 + fname1 + '\n')	# nickname plus firstname
				for birth in birthday:
					if birth == '' and ' ' and '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(nname1 + fname1 + birth + '\n') # nickname plus firstname plus birthday
			for birth in birthday:
				if birth == '' and ' ' and '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1 + birth + '\n')	# nickname plus birthday vice-versa
						f.write(birth + nname1 + '\n')

	for lname1 in lname:
		if lname1 == '' and ' ' and '  ':
			pass
		else:
			with open(filename, 'a') as f:			
				f.write(lname1 + '\n')	# lastname
			for fname1 in fname:
				with open(filename, 'a') as f:
					f.write(lname1 + fname1 + '\n') # lastname plus firstname
				for birth in birthday:
					if birth == '' and ' ' and '  ':
						pass
					else:
						with open(filename, 'a') as f:
							f.write(lname1 + fname1 + birth + '\n')	# lastname plus firstname plus birthday
			for nname1 in nname:
				if nname1 == '' and ' ' and '  ':
					pass
				else:
					with open(filename, 'a') as f:
						f.write(lname1 + nname1 + '\n') # lastname plus nickname
					for birth in birthday:
						if birth == '' and ' ' and '  ':
							pass
						else:
							with open(filename, 'a') as f:
								f.write(lname1 + nname1 + birth + '\n')
			for birth in birthday:
				if birth == '' and ' ' and '  ':
					pass
				else:
					with open(filename, 'a') as f:
						f.write(lname1 + birth + '\n')	# lastname plus birthday vice-versa
						f.write(birth + lname1 + '\n')



	''' 		REVERSED PART		'''
	for fname1 in fname:
		with open(filename, 'a') as f:			
			f.write(fname1[::-1] + '\n')		# firstname
		for lname1 in lname:
			if lname1 == '' and ' ' and '  ':
				break		
			else:			
				with open(filename, 'a') as f:		
					f.write(fname1[::-1] + lname1[::-1] + '\n')	# firstname plus lastname						
				for birth in birthday:
					if birth == '' and ' ' and '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(fname1[::-1] + lname1[::-1] + birth + '\n')	# firstname plus lastname plus birthday
		for nname1 in nname:
			if nname1 == '' and ' ' and '  ':
				break
			else:
				with open(filename, 'a') as f:
					f.write(fname1[::-1] + nname1[::-1] + '\n')			# firstname plus nickname 
				for birth in birthday:
					if birth == '' and ' ' and '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(fname1[::-1] + nname1[::-1] + birth + '\n') # firstname plus lastname plus birthday
		for birth in birthday:
			if birth == '' and ' ' and '  ':
				break
			else:
 				with open(filename, 'a') as f:
 					f.write(fname1[::-1] + birth + '\n')
 					f.write(birth + fname1[::-1] + '\n')	# firstname plus birthday vice-versa
	for nname1 in nname:
		if nname1 == '' and ' ' and '  ':
			break
		else:
			with open(filename, 'a') as f:			
				f.write(nname1[::-1] + '\n')	# nickname
			for lname1 in lname:
				if lname1 == '' and ' ' and '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1[::-1] + lname1[::-1] + '\n')	# nickname plus lastname
			for birth in birthday:
				if birth == '' and ' ' and '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1[::-1] + lname1[::-1] + birth + '\n')	# nickname plus lastname plus birthday
		for fname1 in fname:
			with open(filename, 'a') as f:
				f.write(nname1[::-1] + fname1[::-1] + '\n')	# nickname plus firstname
			for birth in birthday:
				if birth == '' and ' ' and '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1[::-1] + fname1[::-1] + birth + '\n') # nickname plus firstname plus birthday
		for birth in birthday:
			if birth == '' and ' ' and '  ':
				break
			else:
				with open(filename, 'a') as f:
					f.write(nname1[::-1] + birth)	# nickname plus birthday vice-versa
					f.write(birth + nname1[::-1] + '\n')

	for lname1 in lname:
		if lname1 == '' and ' ' and '  ':
			break
		else:
			with open(filename, 'a') as f:			
				f.write(lname1[::-1] + '\n')	# lastname
			for fname1 in fname:
				with open(filename, 'a') as f:
					f.write(lname1[::-1] + fname1[::-1] + '\n') # lastname plus firstname
			for birth in birthday:
				if birth == '' and ' ' and '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(lname1[::-1] + fname1[::-1] + birth + '\n')	# lastname plus firstname plus birthday
		for nname1 in nname:
			if nname1 == '' and ' ' and '  ':
				break
			else: 
				with open(filename, 'a') as f:
					f.write(lname1[::-1] + nname1[::-1] + '\n') # lastname plus nickname
				for birth in birthday:
					if birth == '' and ' ' and '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(lname1[::-1] + nname1[::-1] + birth + '\n')
		for birth in birthday:
			if birth == '' and ' ' and '  ':
				break
			else:
				with open(filename, 'a') as f:
					f.write(lname1[::-1] + birth + '\n')	# lastname plus birthday vice-versa
					f.write(birth + lname1[::-1] + '\n')


def combination_digits(fname, nname, lname, filename, n):
	if n == 2:
		x = 10
		y = 100
	elif n == 3:
		x = 100
		y = 1000
	elif n == 4:
		x = 1000
		y = 10000
	elif n == 5:
		x = 10000
		y = 100000

	for fname1 in fname:
		for n in range(x, y):
			with open(filename, 'a') as f:			
				f.write(fname1 + str(n) + '\n')		# firstname numbers
		for lname1 in lname:
			if lname1 == '' and ' ' and '  ':
				break
			else:
				for n in range(x, y):					
					with open(filename, 'a') as f:		
						f.write(fname1 + lname1 + str(n) + '\n')	# firstname plus lastname numbers
		for nname1 in nname:
			if nname1 == '' and ' ' and '  ':
				break
			else:
				for n in range(x, y):
					with open(filename, 'a') as f:
						f.write(fname1 + nname1 + str(n) + '\n') # firstname plus nickname numbers

	for nname1 in nname:
		if nname1 == '' and ' ' and '  ':
			break
		else:
			for n in range(x, y):						
				with open(filename, 'a') as f:			
					f.write(nname1 + str(n) + '\n')	# nickname numbers
		for lname1 in lname:
			if lname1 == '' and ' ' and '  ':
				break
			else:
				for n in range(x, y):
					with open(filename, 'a') as f:
						f.write(nname1 + lname1 + str(n) +'\n')	# nickname plus lastname numbers
		for fname1 in fname:
			for n in range(x, y):
				with open(filename, 'a') as f:
					f.write(nname1 + fname1 + str(n) + '\n')	# nickname plus firstname numbers

	for lname1 in lname:
		if lname1 == '' and ' ' and '  ':
			break
		else:
			for n in range(x, y):
				with open(filename, 'a') as f:			
					f.write(lname1 + str(n) + '\n')	# lastname numbers
		for fname1 in fname:
			for n in range(x, y):
				with open(filename, 'a') as f:
					f.write(lname1 + fname1 + str(n) + '\n') # lastname plus firstname numbers
		for nname1 in nname:
			if nname1 == '' and ' ' and '  ':
				break
			else:
				for n in range(x, y):
					with open(filename, 'a') as f:
						f.write(lname1 + nname1 + str(n) + '\n') # lastname plus nickname numbers