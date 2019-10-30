import requests
import json
import csv
import xlrd
import time

output = 'json'
url = 'https://maps.googleapis.com/maps/api/geocode/'+output+'?'+'address='

#addr = 'Inorbit Mall APIIC Software Layout, Mindspace, Madhapur Madhapur Hyderabad, Telangana'

'''
with open("/home/tapas/Desktop/Seoul_lat_long.csv","r") as f:
	for line in f:
		word = line.split(',')
		print word[0]
		print ('\n')
'''		
count = 894
wf = open("latlong_file_seoul","w")
while count<=2500:
	url = 'https://maps.googleapis.com/maps/api/geocode/'+output+'?'+'address='
	book = xlrd.open_workbook('/home/tapas/Downloads/SeoulLatlong.xlsx')
	first_sheet = book.sheet_by_index(0)
	address = first_sheet.cell(count,0)
	#print address.value
	name = first_sheet.cell(count,12).value
	addr =  address.value
	for val in addr.split(' '):
		url=url+val+'+'
	ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
	s = requests.Session()
	freekey = 'AIzaSyBDh3uEyZc1IEEa_NBLYU8EJeB3dz-wCx4'
	url = url + "&apikey=" + freekey

	req = s.get(url)
	time.sleep(3)
	#print (req.url)
	try: 
            reqdata = json.loads(req.text)
            full_addr = reqdata['results']
            try:
                final_addr = full_addr[0]
                res = final_addr['geometry']
                res1 = res['location']
                lat = res1['lat']
                lon = res1['lng']
            except IndexError:
                lat = 0.0
                lon = 0.0	
	except ValueError:
            lat = 0.0
            lon = 0.0	
		
	print "address is " + str(lat)+ " " +str(lon)
	wf.write(str(name))
	wf.write(',')
	wf.write(str(lat))
	wf.write(',')
	wf.write(str(lon))
	wf.write('\n')
	count = count +1
#with open('jdata.txt','w+') as outfile:
	#json.dump(full_addr[0],outfile)
