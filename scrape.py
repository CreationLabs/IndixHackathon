import urllib      
import csv
from bs4 import BeautifulSoup
import simplejson as json
import re
MAIN_JSON = {}
TAG_JSON = {}

outfile = open('scraped.json','w')

def crawlWeb(url):
  print "URL to be crawled : ",url
  try:
    f = urllib.urlopen(url) 
    soup = BeautifulSoup(f)
    #print soup
    mainJson = []
    pattern = re.compile(r'<a.*/a>')
    for task in pattern.findall(str(soup)):
      print task
    return "done"
  except:
    print "Error while crawling" 	
    return {} 

def addToDB(x,json):
  MAIN_JSON[x] = (json)
"""
with open('indexFile.tsv','rb') as tsvin:
  tsvin = csv.reader(tsvin, delimiter='\t')
  line = 0
  for row in tsvin:
      if line>3 and line< 2705:
	line+=1
	continue
      PorL = row[1]
      ajson = crawlWeb(row[2])    
      addToDB(row[0],ajson)
      line+=1
      
json.dump(MAIN_JSON,outfile,sort_keys=True,indent=4)
      #"http://www.dickssportinggoods.com/product/index.jsp?productId=13215516"
"""
print crawlWeb("http://www.shopwss.com/womens/athletic/?style=Running&primarycolor=Pink%7cBrown%7cBlack")
