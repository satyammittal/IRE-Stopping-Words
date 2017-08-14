import os                                                                                                             
import json
import operator
def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(subdir + "/" + file)                                                                         
    return r

mn = list_files('extracted')
counter = {}
number = 0
check_word = {}
check_doc = {}
for file in mn:

	with open(file) as f:
		for line in f:
			check_word = {}
			jfile = json.loads(line)
			text = jfile['text']
			number+=1

			if text != None:
				for word in text.split():
					if word in counter:
						counter[word]+=1
					else:
						counter[word]=1
					if word in check_word:
						check_word[word]+=1
					else:
						check_word[word]=1
        	for a in check_word:
				if a in check_doc:
					check_doc[a]+=1
				else:
					check_doc[a]=1

result = {}
for a in check_doc:
    result[a]=counter[a]*check_doc[a]*check_doc[a]
sorted_c = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
number=50
for d in sorted_c:
    number-=1
    if number<0:
        break

    print d[0],':',d[1]
number=50
for d in sorted_c:
    number-=1
    if number<0:
        break

    print d[0]

