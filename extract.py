import csv


def getJson(row):
  index = row.find('.com') + 4
  host = row[:index]
  others = row[index:].split('/') #Supposing that / means sub url divisions



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



