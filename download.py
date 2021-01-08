#!/usr/bin/env python
import pprint
import os.path
import requests
import urllib2
import time
from bs4 import BeautifulSoup

print 'Searching'

url = 'https://audioboom.com/channel/nosuchthingasafish?page=1'
response = urllib2.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "html.parser")

links = soup.findAll('a', href=lambda href: href and "posts" in href, attrs={'class':'l-abs-fill-all'})

for link in links:
	href = link['href']
	download_url = href + '.mp3'
	
	filename = './downloaded/' + download_url[download_url.rindex('/')+1:]

	if (os.path.exists(filename) != True):
		print 'Downloading ' + filename

		filedata = urllib2.urlopen(download_url)
		datatowrite = filedata.read()
		with open(filename, 'wb') as f:
			f.write(datatowrite)
		time.sleep(1)
	else:
		print 'Skipping ' + filename