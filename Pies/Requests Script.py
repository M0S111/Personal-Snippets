import os,sys,requests

#sys.argv[1]

feedback = []

loc = '/storage/emulated/0/CPP Projects/'

for txt in os.listdir(loc):
	feedback.append(txt)
	
#print(feedback)

data = {'name':'','date':'','feedback':''}

for file in feedback:
	with open(os.path.join(loc,file),'r') as content:
				for i in data:
					for line in content:
						
						data[i] = line.split('\n')
			
		
print(data)