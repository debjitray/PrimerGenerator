import sys
import re
from collections import defaultdict
actual = defaultdict(int)
new = defaultdict(int)

def hamming2(s1, s2):
	assert len(s1) == len(s2)
	return sum(c1 != c2 for c1, c2 in zip(s1, s2))



k =  open(sys.argv[1],"r")
k2 = open(sys.argv[2],"r")


for line in k2:
	line=line.rstrip("\n")
	actual[line]+=1

for line in k:
	line=line.rstrip("\n")
	if line not in actual:
#		if re.search("AA", line) or re.search("CC", line) or re.search("GG", line) or re.search("TT", line):
#			pass
#		else:
		new[line]+=1

new2=defaultdict(int)
igloo=defaultdict(int)

for keys in new:
	new2[keys]+=1
	
#print(igloo)

for keys in actual:
	new2[keys]+=1

for keys in new:
	arrx=[]
	for alba in new2:
		if keys != alba:
			arrx.append(hamming2(keys,alba))
	count=len(arrx)
	for j in arrx:
		if int(j) < 3 :
			count=count-1
#	print (str(len(arrx))+"\t"+str(count))
	if count == len(arrx):
		igloo[keys]+=1


#indi = defaultdict(int)
#for keys in igloo:
#	indi[keys]+=1

#for x in indi:
#	print(x)

for g in igloo:
	print(g)
