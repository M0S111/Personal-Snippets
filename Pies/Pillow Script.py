from PIL import Image
import os,sys

#loc = sys.argv[1]

count = 0

for root, dirs, files in os.walk('/storage/emulated/0/Pictures/B side/', topdown=False):
   for name in files:
   	count += 1
   	im = Image.open(os.path.join(root,name))
   	im.rotate(270).resize((128,128)).save(root+name,'JPEG')


#'Bitch {}.jpeg'.format(count)