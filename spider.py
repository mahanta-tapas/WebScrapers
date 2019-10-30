import os
import requests
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
import json

	
ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}



err_list = []

city = "Bhubaneswar"
city_file = city + '.txt'
rsf =  open (city_file,"w+")

def saveRefToFile(req,filename):
	path = "home/tapas/Desktop/" + filename
	print (path)
	with open("/home/tapas/Desktop/Wikinews.html","wb") as f:
		for chunk in req.iter_content(512):
			f.write(chunk)

def getRequest(url):
	return requests.get(url,stream=True)

def isLastPage(response):
	f = response.content	
	soup = BeautifulSoup((f))	
	header = soup.find("head")
	pageExists = header.find_all("link",rel="next")	
	if  not pageExists:
		print ("this is last page")
		return True
	else:
		#print "Page Exists is True"  
		return False		
	
def makeRequest(url,PageNumber):
	payload = OrderedDict([('page',PageNumber)])
	s = requests.Session()
	return s.get(url,headers=ua,params=payload)
def getTitle(res_num):	
	s = BeautifulSoup (res_num['snippet'])	
	_title = s.find("a",'result-title')
	title = _title.attrs['title']	
	return title
def getLat(res_num):
	return str(res_num['lat'])
def getLon(res_num):
	return str(res_num['lon'])
def getRating(res_num):
	return(str(res_num['rating']))

def getCost(res_num):
	s = BeautifulSoup (res_num['snippet'])
	_cost = s.find("div",'grey-text')
	if _cost:
		cost = _cost.text
	else:
		cost = '0'	
	return str(cost.encode('utf-8'))		

def writeFile(title,lat,lon,rating,cost):
	rsf.write(title+' ')
	rsf.write(lat+' ')
	rsf.write(lon+' ')
	rsf.write(rating+' ')
	rsf.write(cost)
	rsf.write('\n')

def extractResponse(response,page):
	f = response.content	
	soup = BeautifulSoup((f))	
	header = soup.find("head")
	search_results = soup.find(id="orig-search-list")
	data = search_results.find_all("a","result-title")
	print("showing results for PageNumber " + str(page))
	lat = soup.find_all("script")
	matchobj = re.search( '(zomato.DailyMenuMap.mapData)(\s)*(=)(.*?)(;+(\s)*zomato.DailyMenuMap.center)', str(lat[8]), re.M|re.I|re.DOTALL)
	print matchobj
        return matchobj				

matchobj = re.search('(BRN-CLG-CHQ PAID TO)(.*?)'('\n'),line)

def getValues(matchobj,page):
	counter = 1	
	if matchobj:		
		j = json.loads(matchobj.group(4))
		#print j
		rsf.write("PageNumber : "+str(page)+'\n')		
		while str(counter) in j:
			res_num = j[str(counter)]
			title = getTitle(res_num)
			lat =   getLat(res_num)
			lon =   getLon(res_num)
			cost =  getCost(res_num)
			rating = getRating(res_num)
			writeFile(title,lat,lon,rating,cost)
			print title	
			counter+=1
	else:
		err_list.append(page) 
		print 'no results for ' + str(page)


if __name__ =='__main__':
	
	url = "http://www.zomato.com/" +city+ "/restaurants"
	PageNumber = 0
	while True:
		PageNumber += 1
		response = makeRequest(url,PageNumber)
		matchobj = extractResponse(response,PageNumber)
		getValues(matchobj,PageNumber)
		if isLastPage(response):
			break;
	if (len(err_list)!= 0):			
		print " error in files " 
		for lis in err_list:
			print lis
		for page in err_list:
			response = makeRequest(url,page)
			matchobj = extractResponse(response,page)
			if matchobj:
				err_list.remove(page)
				getValues(matchobj,page)
			else:
				print " Page " + str(page) + "failed again"	
            
			if (len(err_list)== 0):
				break;	
	else:
		print "all pages are good"				
