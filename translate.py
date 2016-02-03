import os
import re
import fileinput
import string
import http.client

google="translate.google.cn"
enCN="/#en/zh-CN/"
reg=re.compile("[a-z]+")

tapi=http.client.HTTPConnection(google)

def toword(line):
	L=[]
	w=""
	for i in range(len(line)):
		if line[i]==' ':
			if len(w)>0:
				m = reg.search(w.lower())
				if m :
					a=m.group(0)
					if len(a)>2:
						L.append(a)
				w=""
		else:
			w+=line[i]
	return L

def google_translate(word):
	tapi.request("GET",enCN+word)
	response=tapi.getresponse()
	cnword=""
	while not response.closed:
		cnword=cnword+response.read(200)
	return cnword
		
def translate():
	for line in fileinput.input():
		for word in toword(line):
			print word
			
if __name__=="__main__":
	translate()
	tapi.close()