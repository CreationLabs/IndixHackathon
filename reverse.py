import simplejson as json
REVERSE_KEYS = {}
REVERSE_TAGS = {}
__DEBUG__ = True # True for development

infile = open('dump.json','r')
outfile1 = open('reversekeys.json','w')
outfile2 = open('reversetags.json','w')

data = json.load(infile)
for datum in data.keys():
	url = data[datum].keys()[0]
	PorL = data[datum][url]['result']
	keys = data[datum][url]['key']
	tags = data[datum][url]['tags']
	for key in keys:
		if key[0] not in REVERSE_KEYS.keys():
			REVERSE_KEYS[key[0]] = []
		element = {}
		element['result'] = PorL
		element['url'] = url
		REVERSE_KEYS[key[0]].append(element)
	for tag in tags:
		if len(tag) > 1:
			if tag not in REVERSE_TAGS.keys():
				REVERSE_TAGS[tag] = []
			element = {}
			element['result'] = PorL
			element['url'] = url
			REVERSE_TAGS[tag].append(element)
json.dump(REVERSE_TAGS,outfile2,sort_keys=True,indent=4)
json.dump(REVERSE_KEYS,outfile1,sort_keys=True,indent=4)

