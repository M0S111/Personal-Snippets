def albumer(art_name,al_name,tr_num):
    discog={'Album':al_name,'Artist':art_name,'Tracks':tr_num}
    return discog

al=albumer('Eminem','Marshal Mathers LP','14')

print(al)

al2=albumer('Dr.Dre','The Chronic','19')

print(al2)

while True:
    al=input('\nEnter album name. Press q to exit. ')

    if al=='q':
        break

    ar=input('\nEnter artist name. Press q to exit. ')

    if ar=='q':
        break

    tr=input('\nEnter no. of tracks. Press q to exit. ')

    if tr=='q':
        break

    print('\n',albumer(ar,al,tr))

    
