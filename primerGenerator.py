import os

for x in range(100000):
	print(x)
	os.system('python string.py')
	os.system('python All.py All.txt already.txt')
	os.system('python All.py All.txt already.txt >> already.txt')


