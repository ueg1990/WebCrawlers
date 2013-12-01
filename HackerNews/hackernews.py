from bs4 import BeautifulSoup
import re
import urllib2
import os
import json

def getLatestArticles():

	latestArticles = {}

	hackernewsFile = urllib2.urlopen("https://news.ycombinator.com/")
	hackernewsHtml = hackernewsFile.read()
	hackernewsFile.close()

	soup = BeautifulSoup(hackernewsHtml)

	#for row in soup.find_all('td'):
	# for row in soup.find_all('ul', {'class' : 'lcp_catlist'}):
	# 	for title in row.find_all('li'):
	# 		print(title.a.get('title'))

	row = soup.find_all('td', {'class' : 'title'})
	#print row[0]
	for title in row:
	 	if title.a is not None:
	 		#print(title.a.string)
	 		latestArticles[title.a.string] = title.a.get('href')
 	 		
		
	 	#latestArticles.append(title.a.get('href'))

	return latestArticles

result = getLatestArticles()

with open('results.json', 'w') as f:
	json.dump(result, f)

print result['More']
#for key in result.keys():
#	print(key + " " +  result[key])

print(len(result))