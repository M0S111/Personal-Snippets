def latinate():
    
	str = input('Enter your message. ')

	st_edit = str.split()

	for w in st_edit:
	   	
		l = w[0]
	   	
		nw = w[1:]
	   	
		nw = nw + l
	   	
		nw = nw + 'ay'
	   	
		st_edit[st_edit.index(w)] = nw
	   	
		st_edit = ' '.join(st_edit)
	   	
	print('\nYour translated message: {0}'.format(st_edit))
	
latinate()


