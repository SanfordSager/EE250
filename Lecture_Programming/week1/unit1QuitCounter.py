def quitcounter():
	count = 0
	x = input('user input: ')
	while x!='quit':
		x = input('user input:')
		count +=1;
	print('Count: ' + str(count))
