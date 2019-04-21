import display
from os import system as c


def Question():
	display.im_help()
	fname = ''
	fname = input(' (make) >> First name: ')				#	ask for firstname
	while len(fname) < 3:
		fname = input(' (make) >> Needed first name: ')		#	if invalid ask again
	c('clear')
	display.im_help()
	print('\tFirst Name => ' + fname.capitalize() + '\n')

	lname = input(' (make) >> Last name: ')					#	ask for lastname
	c('clear')
	if lname == '' or lname == ' ' or lname == '  ':
		display.im_help()
		print('\tLast Name => not set\n')
	else:
		display.im_help()
		print('\tLast Name => ' + lname.capitalize() + '\n')

	nname = input(' (make) >> Nickname: ')					#	ask for nickname
	c('clear')
	if nname == '' or nname == ' ' or nname == '  ':
		display.im_help()
		print('\tNickname => not set\n')
	else:
		display.im_help()
		print('\tNickname => ' + nname.capitalize() + '\n')

	birth = input(' (make) >> Birthday(mmddyyyy): ').strip()#	ask for birthday
	c('clear')
	if birth == '' or birth == ' ' or birth == '  ':
		display.im_help()
		print('\tBirthday => not set\n ')
	else:
		display.im_help()
		print('\tBirthday => ' + birth[0:2], birth[2:4], birth[4:] + '\n')

	pet = input(' (make) >> Pet name: ')					# ask for pet name
	c('clear')
	if pet == '' or pet == ' ' or pet == '  ':
		display.im_help()
		print('\tPet => not set\n')
	else:
		display.im_help()
		print('\tPet => ' + pet.capitalize() + '\n')
	if lname == '' and nname == '' and pet == '' and birth == '':
		digits = 'y'
	else:
		digits = input(' (make) >> Would you like to add number in every last word?(y/n | default=N): ').lower()
	n = 0
	if digits == 'y':
		n = int(input(' (make) >> Digit number in the end(e.g if 2, then name10, name11, ...): '))
	reverse = input(' (make) >> Do you want to reverse the names?(y/n | default=N): ').lower()
	filename = input(' (make) >> Filename: ') + '.txt'
	return fname, lname, nname, birth, pet, filename, digits, n, reverse


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


def names_process(fname, lname, nname, pet):
	fnames = [fname.upper(), fname.lower(), fname.capitalize()]
	lnames = [lname.upper(), lname.lower(), lname.capitalize()]
	nnames = [nname.upper(), nname.lower(), nname.capitalize()]
	pet = [pet.upper(), pet.lower(), pet.capitalize()]
	return fnames, lnames, nnames, pet


def combinations(fname, lname, nname, pet, birthday, filename):
	for fname1 in fname:
		with open(filename, 'a') as f:			
				f.write(fname1 + '\n')		# firstname						
		for lname1 in lname:
			if lname1 == '' or lname1 == ' ' or lname1 == '  ':
				break
			else:
				with open(filename, 'a') as f:											
					f.write(fname1 + lname1 + '\n')	# firstname plus lastname
					f.write(fname1 + '_' + lname1 + '\n')	# with underscore
				for birth in birthday:
					if birth == '' or birth == ' ' or birth == '  ':
						pass
					else:
						with open(filename, 'a') as f:
							f.write(fname1 + lname1 + birth + '\n')	# firstname plus lastname plus birthday
		for nname1 in nname:
			if nname1 == '' or nname1 == ' ' or nname1 == '  ':
				break
			else:
				with open(filename, 'a') as f:
					f.write(fname1 + nname1 + '\n')			# firstname plus nickname
					f.write(fname1 + '_' + nname1 + '\n')	# with underscore
				for birth in birthday:
					if birth == '' or birth == ' ' or birth == '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(fname1 + nname1 + birth + '\n') # firstname plus lastname plus birthday
		for birth in birthday:
			if birth == '' or birth == ' ' or birth == '  ':
				pass
			else:
				with open(filename, 'a') as f:
					f.write(fname1 + birth + '\n')
					f.write(fname1 + '_' + birth + '\n')	
					f.write(birth + fname1 + '\n')		# firstname plus birthday vice-versa
					f.write(birth + '_' + fname1 + '\n')# with underscore
		for petn in pet:
				if petn == '' or petn == ' ' or petn == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(fname1 + petn + '\n') # firstname plus pet name
						f.write(fname1 + '_' + petn + '\n') # with underscore

	for nname1 in nname:
		if nname1 == '' or nname1 == ' ' or nname1 == '  ':
			break
		else:						
			with open(filename, 'a') as f:			
				f.write(nname1 + '\n')	# nickname
			for lname1 in lname:
				if lname1 == '' or lname1 == ' ' or lname1 == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1 + lname1 + '\n')	# nickname plus lastname
						f.write(nname1 + '_' + lname1 + '\n')	# with underscore
					for birth in birthday:
						if birth == '' or birth == ' ' or birth == '  ':
							break
						else:
							with open(filename, 'a') as f:
								f.write(nname1 + lname1 + birth + '\n')	# nickname plus lastname plus birthday
			for fname1 in fname:
				with open(filename, 'a') as f:
					f.write(nname1 + fname1 + '\n')	# nickname plus firstname
					f.write(nname1 + '_' + fname1 + '\n') # with underscore
				for birth in birthday:
					if birth == '' or birth == ' ' or birth == '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(nname1 + fname1 + birth + '\n') # nickname plus firstname plus birthday
			for birth in birthday:
				if birth == '' or birth == ' ' or birth == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1 + birth + '\n')	# nickname plus birthday vice-versa
						f.write(nname1 + '_' + birth + '\n')
						f.write(birth + nname1 + '\n')
						f.write(birth + '_' + nname1 + '\n') # with underscore
			for petn in pet:
				if petn == '' or petn == ' ' or petn == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1 + petn + '\n') # nickname plus pet name
						f.write(nname1 + '_' + petn + '\n') # with underscore

	for lname1 in lname:
		if lname1 == '' or lname1 == ' ' or lname1 == '  ':
			pass
		else:
			with open(filename, 'a') as f:			
				f.write(lname1 + '\n')	# lastname
			for fname1 in fname:
				with open(filename, 'a') as f:
					f.write(lname1 + fname1 + '\n') # lastname plus firstname
					f.write(lname1 + '_' + fname1 + '\n') # with underscore
				for birth in birthday:
					if birth == '' or birth == ' ' or birth == '  ':
						pass
					else:
						with open(filename, 'a') as f:
							f.write(lname1 + fname1 + birth + '\n')	# lastname plus firstname plus birthday
			for nname1 in nname:
				if nname1 == '' or nname1 == ' ' or nname1 == '  ':
					pass
				else:
					with open(filename, 'a') as f:
						f.write(lname1 + nname1 + '\n') # lastname plus nickname
						f.write(lname1 + '_' + nname1 + '\n') # with underscore
					for birth in birthday:
						if birth == '' or birth == ' ' or birth == '  ':
							pass
						else:
							with open(filename, 'a') as f:
								f.write(lname1 + nname1 + birth + '\n')
			for birth in birthday:
				if birth == '' or birth == ' ' or birth == '  ':
					pass
				else:
					with open(filename, 'a') as f:
						f.write(lname1 + birth + '\n')	# lastname plus birthday vice-versa
						f.write(lname1 + '_' + birth + '\n')
						f.write(birth + lname1 + '\n')
						f.write(birth + '_' + lname1 + '\n') # with underscore
			for petn in pet:
				if petn == '' or petn == ' ' or petn == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(lname1 + petn + '\n') # lastname plus pet name
						f.write(lname1 + '_' + petn + '\n') # with underscore

	for petn in pet:
		if petn == '' or petn == ' ' or petn == '  ':
			break
		else:
			with open(filename, 'a') as f:
				f.write(petn + '\n')	# pet name
			for fname1 in fname:
				with open(filename, 'a') as f:
					f.write(petn + fname1 + '\n') 	# pet name plus first name
					f.write(petn + '_' + fname1 + '\n')	# with underscore
			for lname1 in lname:
				if lname1 == '' or lname1 == ' ' or lname1 == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(petn + lname1 + '\n') # pet name plus last name
						f.write(petn + '_' + lname1 + '\n') # with underscore
			for nname1 in nname:
				if nname1 == '' or nname1 == ' ' or nname1 == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(petn + nname1 + '\n') # pet name plus nick name
						f.write(petn + '_' + nname1 + '\n') # with underscore 

		
def combinations_reverse(fname, lname, nname, birthday, filename):
	for fname1 in fname:
		with open(filename, 'a') as f:			
			f.write(fname1[::-1] + '\n')		# firstname
		for lname1 in lname:
			if lname1 == '' or lname1 == ' ' or lname1 == '  ':
				break		
			else:			
				with open(filename, 'a') as f:		
					f.write(fname1[::-1] + lname1[::-1] + '\n')	# firstname plus lastname						
				for birth in birthday:
					if birth == '' or birth == ' ' or birth == '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(fname1[::-1] + lname1[::-1] + birth + '\n')	# firstname plus lastname plus birthday
		for nname1 in nname:
			if nname1 == '' or nname1 == ' ' or nname1 == '  ':
				break
			else:
				with open(filename, 'a') as f:
					f.write(fname1[::-1] + nname1[::-1] + '\n')			# firstname plus nickname 
				for birth in birthday:
					if birth == '' or birth == ' ' or birth == '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(fname1[::-1] + nname1[::-1] + birth + '\n') # firstname plus lastname plus birthday
		for birth in birthday:
			if birth == '' or birth == ' ' or birth == '  ':
				break
			else:
 				with open(filename, 'a') as f:
 					f.write(fname1[::-1] + birth + '\n')
 					f.write(birth + fname1[::-1] + '\n')	# firstname plus birthday vice-versa
	for nname1 in nname:
		if nname1 == '' or nname1 == ' ' or nname1 == '  ':
			break
		else:
			with open(filename, 'a') as f:			
				f.write(nname1[::-1] + '\n')	# nickname
			for lname1 in lname:
				if lname1 == '' or lname1 == ' ' or lname1 == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1[::-1] + lname1[::-1] + '\n')	# nickname plus lastname
			for birth in birthday:
				if birth == '' or birth == ' ' or birth == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1[::-1] + lname1[::-1] + birth + '\n')	# nickname plus lastname plus birthday
		for fname1 in fname:
			with open(filename, 'a') as f:
				f.write(nname1[::-1] + fname1[::-1] + '\n')	# nickname plus firstname
			for birth in birthday:
				if birth == '' or birth == ' ' or birth == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(nname1[::-1] + fname1[::-1] + birth + '\n') # nickname plus firstname plus birthday
		for birth in birthday:
			if birth == '' or birth == ' ' or birth == '  ':
				break
			else:
				with open(filename, 'a') as f:
					f.write(nname1[::-1] + birth)	# nickname plus birthday vice-versa
					f.write(birth + nname1[::-1] + '\n')

	for lname1 in lname:
		if lname1 == '' or lname1 == ' ' or lname1 == '  ':
			break
		else:
			with open(filename, 'a') as f:			
				f.write(lname1[::-1] + '\n')	# lastname
			for fname1 in fname:
				with open(filename, 'a') as f:
					f.write(lname1[::-1] + fname1[::-1] + '\n') # lastname plus firstname
			for birth in birthday:
				if birth == '' or birth == ' ' or birth == '  ':
					break
				else:
					with open(filename, 'a') as f:
						f.write(lname1[::-1] + fname1[::-1] + birth + '\n')	# lastname plus firstname plus birthday
		for nname1 in nname:
			if nname1 == '' or nname1 == ' ' or nname1 == '  ':
				break
			else: 
				with open(filename, 'a') as f:
					f.write(lname1[::-1] + nname1[::-1] + '\n') # lastname plus nickname
				for birth in birthday:
					if birth == '' or birth == ' ' or birth == '  ':
						break
					else:
						with open(filename, 'a') as f:
							f.write(lname1[::-1] + nname1[::-1] + birth + '\n')
		for birth in birthday:
			if birth == '' or birth == ' ' or birth == '  ':
				break
			else:
				with open(filename, 'a') as f:
					f.write(lname1[::-1] + birth + '\n')	# lastname plus birthday vice-versa
					f.write(birth + lname1[::-1] + '\n')	# REVERSED


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
			if lname1 == '' or lname1 == ' ' or lname1 == '  ':
				break
			else:
				for n in range(x, y):					
					with open(filename, 'a') as f:		
						f.write(fname1 + lname1 + str(n) + '\n')	# firstname plus lastname numbers
		for nname1 in nname:
			if nname1 == '' or nname1 == ' ' or nname1 == '  ':
				break
			else:
				for n in range(x, y):
					with open(filename, 'a') as f:
						f.write(fname1 + nname1 + str(n) + '\n') # firstname plus nickname numbers

	for nname1 in nname:
		if nname1 == '' or nname1 == ' ' or nname1 == '  ':
			break
		else:
			for n in range(x, y):						
				with open(filename, 'a') as f:			
					f.write(nname1 + str(n) + '\n')	# nickname numbers
		for lname1 in lname:
			if lname1 == '' or lname1 == ' ' or lname1 == '  ':
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
		if lname1 == '' or lname1 == ' ' or lname1 == '  ':
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
			if nname1 == '' or nname1 == ' ' or nname1 == '  ':
				break
			else:
				for n in range(x, y):
					with open(filename, 'a') as f:
						f.write(lname1 + nname1 + str(n) + '\n') # lastname plus nickname number