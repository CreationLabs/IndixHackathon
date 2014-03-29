import csv
__DEBUG__ = True # False if production

def getJson(row):
  row = row[2]
  index = row.index('.com') + 4
  host = row[:index]

  if __DEBUG__:
    print 'URL : ', row
    print 'Host : ',host
  others = row[index:].split('/') #Supposing that / means sub url divisions
  last = others[-1]
  if __DEBUG__:
    print "Others : ", others
    print "Last : ",last
  queryparams = last
  others.append(last.split('?')[0])
  beforeLast = '/'.join(others[:-1])
  if __DEBUG__:
    print "BeforeLast : ",beforeLast
    print "Queryparams: ",queryparams
  if len(queryparams) > 0:
    if queryparams.split(';') > 1:
      DELIMITER = ';'
    elif queryparams.split('&') > 1:
      DELIMITER = '&'
    queryparams = queryparams.split(DELIMITER)
    queries = []
  queries = []
    for query in queryparams:
      query = tuple(query.split('='))
      queries.append(query)
  else:
    queryparams = {}
  mainJson = {}
  mainJson[host] = {}
  mainJson[host][beforeLast] = queries
  print mainJson
  return mainJson
  
def addToDB(json):
  print 'Timepass'

with open('indexFile.tsv','rb') as tsvin:
  tsvin = csv.reader(tsvin, delimiter='\t')
  line = 0
  for row in tsvin:
      json = getJson(row)
      addToDB(json)
      line+=1
      raw_input() # Line by line input prompt



