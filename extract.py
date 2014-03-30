import csv
import simplejson as json
from sklearn import svm 
import re
patternSlug = re.compile('[A-Za-z]*(-[A-Za-z]*)+')
patternSlug2 = re.compile('[A-Za-z]*(_[A-Za-z]*)+')

__DEBUG__ = False # False if production
MAIN_JSON = {}
TAG_JSON = {}
KEY_JSON = {}

outfile = open('dump.json','w')
tagfile = open('tag.json','w')
keyfile = open('key.json','w')
#reversefile = open('reverse.json','w')

def getJson(row,PorL,URL):
  row = row[2]
  url = URL
  index = row.index('.com') + 4
  host = row[:index]

  if __DEBUG__:
    print 'URL : ', row
    print 'Host : ',host
  
  others = row[index:].split('/') #Supposing that / means sub url divisions
  last = others[-1]
  tags = others[:-1]
  key = last.split('?')[0]
  
  if __DEBUG__:
    print "Others : ", others
    print "Last : ",last
    print "Last changed :", last.split('?')
  queryparams = '&'.join(last.split('?')[1:])
  others.append(last.split('?')[0])
  beforeLast = '/'.join(others[:-1])

  if __DEBUG__:
    print "BeforeLast : ",beforeLast
    print "Queryparams: ",queryparams
    print others[-1].split('&')
  queries = []
  if len(queryparams) > 0:
    if len(queryparams.split(';')) > len(queryparams.split('&')) :
      DELIMITER = ';'
    else:
      DELIMITER = '&'
    queryparams = queryparams.split(DELIMITER)
    queries = []
    for query in queryparams:
      query = tuple(query.split('='))
      queries.append(query)
  else:
    queryparams = {}
  mainJson = {}
  mainJson[url] = {}
  mainJson[url]["host"] = host
  mainJson[url]["key"] = queries
  mainJson[url]["tags"] = tags
  
  for key_obj in queries:
    if key_obj[0] not in KEY_JSON.keys():
      KEY_JSON[key_obj[0]] = {}
      KEY_JSON[key_obj[0]][PorL] = 1
    else:
      try:
	KEY_JSON[key_obj[0]][PorL]+=1
      except:
	KEY_JSON[key_obj[0]][PorL]=1
 					
  for tag in tags:
    if tag == "":
      continue
    if tag.isdigit():
      tag = "_NUMBER"
    if patternSlug.match(tag) or patternSlug2.match(tag):
      tag = "_SLUG"
    if tag not in TAG_JSON.keys():
      TAG_JSON[tag] = {}
      TAG_JSON[tag]['L'] = 0
      TAG_JSON[tag]['P'] = 0
      TAG_JSON[tag][PorL] = 1
    else:
      try: 
        TAG_JSON[tag][PorL]+=1
      except:
        TAG_JSON[tag][PorL]=1
        
  mainJson[url]["result"] = PorL
  return mainJson
  
def addToDB(x,json):
  MAIN_JSON[x] = (json)


with open('indexFile.tsv','rb') as tsvin:
  tsvin = csv.reader(tsvin, delimiter='\t')
  line = 0
  for row in tsvin:
      PorL = row[1]
      ajson = getJson(row,PorL,row[2])    
      addToDB(row[0],ajson)
      line+=1
      #raw_input() # Line by line input prompt
  json.dump(MAIN_JSON,outfile,sort_keys=True,indent=4)
  json.dump(TAG_JSON,tagfile,sort_keys=True,indent=4)
  json.dump(KEY_JSON,keyfile,sort_keys=True,indent=4)
  #json.dump(REVERSE_JSON,reversefile,sort_keys=True,indent=4)
  #reversefile.close()
  tagfile.close()
  outfile.close()
  print "DONE"




