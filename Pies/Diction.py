import json

my_deets = [{'firstName':'Mohammad',
			'secondName':'Sheharyar',
			'occupation':'Software Engineer',
			'nationality':'PK'
			}]

#with open('deets.json','w') as deets_json:
#	json.dump(my_deets,deets_json,indent=2)

with open('deets.json','r') as deets_json:
	dets = json.load(deets_json)
print(dets)


#deets_json = json.dumps(my_deets)
#print(deets_json)