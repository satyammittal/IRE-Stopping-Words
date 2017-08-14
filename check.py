import os
mn = ['id.stopwords.02.01.2016.txt']
g = {}
for file in mn:
	with open(file) as f:
		for line in f:
			g[line]=1
mn = ['bahasa_sol4.txt']
for file in mn:
	with open(file) as f:
		for line in f:
			if not line in g:
				print line
