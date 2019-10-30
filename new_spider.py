import os
import requests

from bs4 import BeautifulSoup
from collections import OrderedDict


	

def saveRefToFile(req,filename):
	path = "home/tapas/Desktop/" + filename
	print (path)
	with open("/home/tapas/Desktop/Wikinews.html","wb") as f:
		for chunk in req.iter_content(512):
			f.write(chunk)

def getRequest(url):
	return requests.get(url,stream=True)
	

#req = getRequest("http://en.wikinews.org/wiki/Main_Page")	

#saveRefToFile(req,"Wikinews.html")

#with open ("/home/tapas/Desktop/zomato.html","r") as f:
	cityId, area

payload = OrderedDict([('cityId','Hydearabad'),('area','Gachibowli'),('submit','xml'),('disabled','enabled')])
req = requests.get("http://www.foodpanda.in/restaurants",params=payload)
f = req.content	
#print (f)
soup = BeautifulSoup((f))	
with open ("/home/tapas/Desktop/prettyfile.txt","w+") as f:
	f.write(soup.prettify())
print ("the title of the page is ")

#with open("/home/tapas/Desktop/food.txt","wb") as f2:
	#f2.write(soup)	
'''
#with open ("/home/tapas/Desktop/prettyfile.txt","w+") as f:
	#f.write(soup.prettify())

search_results = soup.find(id="orig-search-list")
data = search_results.find_all("a","result-title")

#print (data[0])
for name in data:
	print (name.attrs['title']) 
	'''
'''divContent = soup.find(id="mw-content-text")	

tables = divContent.find_all('table')
f = open ("/home/tapas/Desktop/News","w+")
for tabledata in tables:
	dat = tabledata.find_all('span')
	if len(dat) >= 1:
		res = dat[1]
		f .write(str(res.string))'''


