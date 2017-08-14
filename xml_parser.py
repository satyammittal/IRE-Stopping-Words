import xml.etree.ElementTree as etree
import codecs
import csv
import time
import os
import operator
PATH_WIKI_XML = ''
FILENAME_WIKI = 'hiwiki.xml'
FILENAME_WIKI = 'idwiki-20170801-pages-meta-current.xml'
pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)
totalCount = 0
articleCount = 0
redirectCount = 0
templateCount = 0
title = None
start_time = time.time()
def strip_tag_name(t):
    t = elem.tag
    idx = k = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t
counter = {}
number = 0
check_word = {}
check_doc = {}
for event, elem in etree.iterparse(pathWikiXML, events=('start', 'end')):
    number += 1
    check_word = {}
    if number > 500000:
        break
    tname = strip_tag_name(elem.tag)
    if event == 'start':
        if tname == 'page':
            title = ''
            id = -1
            redirect = ''
            inrevision = False
            ns = 0
        elif tname == 'revision':
            # Do not pick up on revision id's
            inrevision = True
        else:
            if tname == 'title':
                title = elem.text
            elif tname == 'redirect':
                redirect = elem.attrib['title']
            elif tname == 'text':
                text = elem.text
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
    result[a]=counter[a]*check_doc[a]
sorted_c = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
number=50
for d in sorted_c:
    number-=1
    if number<0:
        break

    print d[0],':',d[1]
    