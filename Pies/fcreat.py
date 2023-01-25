fn=r'C:\Users\Abid Sheri\Desktop\Genius.txt'

with open(fn,'w') as f:
    f.write("I'm the best!")
    f.write("\nI kick ass & take names!")
    
with open(fn,'r') as f:
    p=f.read()
    print(p)