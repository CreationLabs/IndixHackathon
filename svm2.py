from sklearn.svm import SVC
from sklearn import svm
import simplejson as json
from levenshtein import editDistance, editDistanceFast
tagfile = open('reversetags.json')
keyfile = open('reversekeys.json')
tags = open('tag.json')
keys = open('key.json')

tagdata = json.load(tagfile)
keydata = json.load(keyfile)
keysarray = json.load(keys)
tagsarray = json.load(tags)
tagmatrix = [[0]*len(tagsarray)]*(len(tagsarray))
#print tagmatrix
for tag in tagsarray.keys():
	print tag		
#for tag in tagdata:

