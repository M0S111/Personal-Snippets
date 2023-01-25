peepz=['him','her','you','them']
peepz.insert(2,'me')
print(peepz.count('me'))
print(peepz.index('you'))
print('we' in peepz)
for folks in peepz:
    if folks=='me':
        truth='the king is among u!!!'
        print(truth.upper())
    else:
        print("U ain't royalty!")
