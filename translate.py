import os
import re
import fileinput

reg=re.compile(".*\w+.*")

def toword(line):
	L=[]
	w=""
	for i in range(len(line)):
		if line[i]==' ':
			if len(w)>0:
				m = reg.search(w)
				L.append(m.group(0))
				w=""
		else:
			w+=line[i]
	return L

def readText2Word():
	d={}
	for line in fileinput.input():
		for word in toword(line):
			if word in d:
				d[word]=d[word]+1
			else:
				d[word]=1
	return d
	
def writeWord2File(dict):
	#sort by count of referece
	count=0
	for v in sorted(dict,key=lambda s:dict[s]):
		print count,v,dict[v]
		count=count+1
	
if __name__=="__main__":
	writeWord2File(readText2Word())