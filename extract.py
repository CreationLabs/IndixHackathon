import csv
with open('indexFile.tsv','rb') as tsvin:
  tsvin = csv.reader(tsvin, delimiter='\t')
  for row in tsvin:
    
