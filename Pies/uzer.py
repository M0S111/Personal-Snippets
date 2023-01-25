prof={}

def car_details(manuf,mod_name,**details):
    nu={}
    nu['Brand']=manuf
    nu['Model']=mod_name
    for a,b in details.items():
        nu[a]=b
    prof.update(nu)




    

car_details('Ford','Mustang',color='cyan')

car_details('Mazda','RX-8',color='magenta')



print(prof)
