import csv


def getJson(row):
  index = row.find('.com') + 4
  host = row[:index]
  others = row[index:].split('/') #Supposing that / means sub url divisions
  last = others[-1]
  beforeLast = '/'.join(others[:-1])
  queryparams = last.split('?')[-1]
  if len(queryparams):
    queryparams.split('&')
    queries = [{a[0] : a[1]} for a.split('=') in queryparams]
  mainJson = {}
  mainJson[host][beforeLast] = queryParams
  print mainJson
  return mainJson
  


with open('indexFile.tsv','rb') as tsvin:
  tsvin = csv.reader(tsvin, delimiter='\t')
  line = 0
  for row in tsvin:
    try:
      json = getJson(row)
      addToDB(json)
      line+=1
    except:
      print 'Error'



