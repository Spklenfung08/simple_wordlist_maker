def banner(): # This prints the banner.
	print('''
 	 ____                                
	| __ )  __ _ _ __   __ _ _ __   __ _ 
	|  _ \\ / _` | '_ \\ / _` | '_ \\ / _` |
	| |_) | (_| | | | | (_| | | | | (_| |
	|____/ \\__,_|_| |_|\\__,_|_| |_|\\__,_|
			Made: March 30, 2019

	This is a simple wordlist maker for targeted profiles.
	Made by Jong!
		''')


def print_help1():
	first_help = '''
	help 	- 	shows this message.
	make 	- 	make wordlist.
	exit 	- 	exits this program.
	clear	-	clears the screen.
	'''
	print(first_help)


def print_help2():
	second_help = '''
	IM	- 	go interactive mode.
	help 	- 	shows this message.
	set 	- 	sets a variable (eg. set fn Larry).
	hvar 	-	shows how to set variables.
	show 	-	shows all variables value.
	back	-	go back.
	'''
	print(second_help)


def print_show(fn, ln, nn, bd, pn):
	the_var = ('''
	First Name = \'%s\'
	Last Name = \'%s\'
	Nickname = \'%s\'
	Birthday(mmddyyyy) = \'%s\'
	Pet name = \'%s\'
	''' %(fn, ln, nn, bd, pn))
	print(the_var)


def print_hvar():
	var_st = '''
	'set fn' for first name.
	'set ln' for last name.
	'set nn' for nickname.
	'set bd' for birthday.
	'set pn' for pet name.
	'''
	print(var_st)


def show_var(profile):
	show = ('''
	First Name 	%s
	Last  Name 	%s
	Nickname	%s
	Birthday	%s
	Pet Name 	%s
	''' %(profile['fn'], profile['ln'], 
		profile['nn'], profile['bd'],
		profile['pn']))
	print(show)

