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
mn = ['out.txt']
counter = {}
number = 0
check_word = {}
check_doc = {}
d_counter = {}
d_counter_num = 0
for file in mn:
	with open(file) as f:
		for line in f:
                        jfile = json.loads(line)
			text = jfile['desc']
                        check_word = {}
			number+=1
                        d_counter_num=0
                        d_counter = {}
			if text != None:
				for word in text.split():
                                        d_counter_num+=1.0
					if not "," in word and not "-" in word and word in counter:
						counter[word]+=1
					elif not "," in word and not "-" in word:
						counter[word]=1
					if not "," in word and not "-" in word and word in check_word:
						check_word[word]+=1
					elif not "," in word and not "-" in word:
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

    print d[0]
