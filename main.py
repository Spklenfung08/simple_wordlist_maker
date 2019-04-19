#!/usr/bin/python3
from os import system as c
from time import sleep as s
import display
import interactive

c('clear')
display.banner()
while True:
	user = input(' >> ').lower()
	if user == 'help':
		display.print_help1()
	elif user == 'make':
		while True:
			user1 = input(' (make) >> ').lower()			#	make the word list.
			if user1 == 'help':								#	this area is for making
				display.print_help2()						#	
			elif user1 == 'im':								#
				fname, lname, nname, birth, pet, filename, digits, n, reverse = interactive.Question()
				day, month, year = interactive.birth_slice(birth)
				dy, yd, my, ym, dm, md = interactive.birth_process(day, month, year)
				birthday = [birth, day, month, year, dy, yd, my, ym, dm, md]
				fnames, lnames, nnames, pets = interactive.names_process(fname, lname, nname, pet)
				interactive.combinations(fnames, lnames, nnames, pets, birthday, filename)
				if reverse == 'y':
					interactive.combinations_reverse(fnames, lnames, nnames, birthday, filename)
				if digits == 'y':
					interactive.combination_digits(fnames, nnames, lnames, filename, n)

			elif user1 == 'back':							#
				break										#
			elif user1 == 'clear':							#
				c('clear')									#			
				display.banner()							#	
			elif user1 == 'hvar':							#
				display.print_hvar()						#
			elif user1 == 'exit':							#
				print('\n\ttype back first then exit\n')		#	end of making word list.
	elif user == 'exit':
		c('clear')
		print('Goodbye!')
		s(2)
		c('clear')
		break
	elif user == 'clear':
		c('clear')
		display.banner()