import numpy as np
import matplotlib.pyplot as plt
import simplejson as json

tagfile = open('tag.json','r')
data = json.load(tagfile)
for datum in data:
	plt.scatter(data[datum]['P'],data[datum]['L'],s=80)
plt.show()