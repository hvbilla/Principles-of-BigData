# -*- coding: utf-8 -*-
import jsonpickle
import json

tweetdetail = list(open('harsha_tweets.json','rt'))

for b in tweetdetail:
	b = json.loads(b)
	try:
		if len(b['entities']['urls']) != 0:
			for h in b['entities']['urls']:
#				with open("hashtags.txt", 'a') as tf:
#					tf.write(h['text'].encode('utf-8'))
				print h['url'].encode('utf8')
	except KeyError:
		pass
