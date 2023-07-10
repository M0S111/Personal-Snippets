import re

def reg_time(s):
	
	time_re = re.compile(r'(\d?\d):(\d{2})\s(\w+)')
	
	t_s = time_re.search(s)
	
	try:
		
		if (t_s.group(1) == '12') and (t_s.group(3) == 'AM'):
				
			return '{0}:{1}'.format('00',t_s.group(2))
			
		elif (t_s.group(1) == '12') and (t_s.group(3) == 'PM'):
				
			return '{0}:{1}'.format('12',t_s.group(2))
			
		elif t_s.group(3) == 'PM':
		
			c = t_s.group(1)
		
			c = int(c)
			
			c = c+12
			
			return '{0}:{1}'.format(str(c),t_s.group(2))
			
		else:
		
			return '{0}:{1}'.format(t_s.group(1),t_s.group(2))
			
	except AttributeError:
			
			return 'Nothing Entered!'
			
		
	

#def time_convert(s):
#	
#	s_e = s.split()
#	
#	if s_e[-1].upper() == 'PM':
#		
#		f = s_e[0]
#		 
#		l = f[:2]
#		
#		l2 = f[2:]
#		 
#		t = int(l)
#		 
#		con = t+12
#	
#		print('{0}{1}'.format(str(con),l2))
#		
#	else:
#		print(s[:-3])
#	
#time_convert('1:40 PM')


	