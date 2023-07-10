import os,sys,re,subprocess

filename = sys.argv[0]

print(filename)

print(os.path.exists(filename))

my_process = subprocess.run(['cat',filename],capture_output='True')

#print(my_process)

print(my_process.stdout.decode())

print(os.environ)
