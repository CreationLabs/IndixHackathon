import numpy as np
import matplotlib.pyplot as plt
import simplejson as json

tagfile = open('tag.json','r')
dumpfile = open('dump.json','r')

data = json.load(tagfile)
dump = json.load(dumpfile)
tot = 0
our = 0
for url in dump:
	tot+=1
	element = dump[url]
	subelem = dump[url][dump[url].keys()[0]]
	tags = subelem['tags']
	res = subelem['result']

	score = 0
	for tag in tags:
		if tag in data:
			if tag == '': continue
			score += data[tag]['P']
			score -= data[tag]['L']
			print tag,score
	if score < 0 :
		oures = 'L'
	else:
		oures = 'P'
	#print oures,res
	#print url
	#raw_input()
	if oures == res :
		our += 1
		pass
	else:
		for tag in tags:
			try:
				if tag == '':continue
				plt.scatter(data[tag]['P'],data[tag]['L'],s=80)
			except:
				pass
		#print url	
print our,tot
print "Accuracy : ",(our*100.0)/tot,"%" 
plt.xlabel("Product Anomalies")
plt.ylabel("Listing Anomalies")
plt.show()