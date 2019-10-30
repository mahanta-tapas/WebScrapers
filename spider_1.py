import os
import requests
import re

from bs4 import BeautifulSoup
from collections import OrderedDict


	
'''
def saveRefToFile(req,filename):
    path = "home/tapas/Desktop/" + filename
    print (path)
    with open("/home/tapas/Desktop/Wikinews.html","wb") as f:
        for chunk in req.iter_content(512):
            f.write(chunk)

def getRequest(url):
    return requests.get(url,stream=True)
	
'''
#req = getRequest("http://en.wikinews.org/wiki/Main_Page")	

#saveRefToFile(req,"Wikinews.html")

#with open ("/home/tapas/Desktop/zomato.html","r") as f:
#cityId, area
dict={}
city = "Bhubaneswar"
url = "http://www.zomato.com/" +city+ "/restaurants"
PageNumber = 0
file_name = city +'.txt'
dcf =  open (file_name,"w+")

while True:
    PageNumber += 1
    payload = OrderedDict([('page',PageNumber)])
    #print (payload.page)
    #payload.city = city	
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
    s = requests.Session()
    req = s.get(url,headers=ua,params=payload,timeout=1000)
    #print (req.url)
    print (req.status_code)
    f = req.content	
    #print (f)
    soup = BeautifulSoup((f))	
    #with open ("/home/tapas/Desktop/prettyfile.txt","w+") as f:
    #f.write(soup.prettify().encode('utf-8'))
    #print ("the title of the page is ")
 

   
    header = soup.find("head")
    #print (header)

    pageExists = header.find_all("link",rel="next")
    if  not pageExists:
        print ("No more results")
        break
    print("showing results for PageNumber " + str(PageNumber))	
    lat = soup.find_all("script")
    with open("script_file.txt","wb") as fw:
        fw.write(lat[8].encode('utf-8'))
    latlist = re.findall('("lat":)(.*?)(,)',str(lat[8]),re.M|re.I)
    if (len(latlist) == 0):
    	latlist = re.findall('("lat":)(.*?)(,)',str(lat[8]),re.M|re.I|re.DOTALL)
    longlist = re.findall('("lon":)(.*?)(,)',str(lat[8]),re.M|re.I)
    if (len(latlist) == 0):
    	longlist = re.findall('("lon":)(.*?)(,)',str(lat[8]),re.M|re.I|re.DOTALL)	

    ratinglist =   re.findall('("rating":)(.*?)(,)',str(lat[8]),re.M|re.I)
    if(len(ratinglist) == 0):
        ratinglist = re.findall('("rating":)(.*?)(,)',str(lat[8]),re.M|re.I|re.DOTALL)

    rating_error = []    
    lat_error = []
    long_error = []	
    if (len(latlist) == 0):
    	lat_error+=[PageNumber]
    if (len(longlist)==0):
    	long_error+=[PageNumber]
    if (len(ratinglist)== 0):
        rating_error+=[PageNumber]

    print(latlist)	
    print (len(latlist))	
    #print (latlist[2])
    search_results = soup.find(id="orig-search-list")
    data = search_results.find_all("a","result-title")

    i=0
    if (len(latlist) != 0):
    	for name in data:
            dcf.write(name.attrs['title']+' ')
            temp = latlist[i]        
            dcf.write(str(temp[1])+' ')
            temp = longlist[i]
            dcf.write(str(temp[1])+' ')
            temp = ratinglist[i]
            dcf.write(str(temp[1])+' ')
            dcf.write('\n')
            i+=1

print 'error in pages for lat ' + str(lat_error)
print 'error in pages for long' + str(long_error)
print 'error in pages for rating' + str(rating_error)

	       	
