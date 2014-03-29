import csv
import simplejson as json
from sklearn import svm 
__DEBUG__ = False # False if production
MAIN_JSON = {}
outfile = open('dump.json','w')

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
  outfile.close()
  print "DONE"




