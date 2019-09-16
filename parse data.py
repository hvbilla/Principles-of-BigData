# -*- coding: utf-8 -*-
import jsonpickle
import json

tweetdet = list(open('harsha_tweets.json','rt'))

for H in tweetdet:
	H = json.loads(t)
	try:
		if len(H['entities']['hashtags']) != 0:
			for p in H['entities']['hashtags']:
				print p['text'].encode('utf8')
	except KeyError:
		pass
