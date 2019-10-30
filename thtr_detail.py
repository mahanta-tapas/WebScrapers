import requests
import json
from collections import OrderedDict

rf = open("restaurant.txt","w+")
def write_in_file(reqdata):
	full_data = reqdata['results']
	for thtr in full_data:
		rf.write(json.dumps(thtr['name']))
		rf.write(json.dumps(thtr['geometry']))
		rf.write(json.dumps(thtr['types']))
		rf.write('\n')
output = 'json'

lat = '17.463586'
lon = '78.3444285'

radius = 50000

place_type = 'restaurant'

freekey = 'AIzaSyCGEZ2hR9Ln9tUlZjMJ8XYCxw6Gsab14rE'

payload = OrderedDict([('location',lat+','+lon),('radius',radius),('types',place_type),('key',freekey),('hasNextPage',True),('nextPage()',True)])
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/'+output
s = requests.Session()
req = s.get(url,params=payload)
print (req.url)

reqdata = json.loads(req.text)
print reqdata['status']

print "next page token is " + str (reqdata['next_page_token']) + "token ends" 
rfn = open("restaurant1.txt","w+")
full_data = reqdata['results']
for thtr in full_data:
	rfn.write(json.dumps(thtr['name']))
	rfn.write(json.dumps(thtr['geometry']))
	rfn.write(json.dumps(thtr['types']))
	rfn.write('\n')


token = json.dumps(reqdata['next_page_token'])
print "type is " + str(token.__class__)
while token:
	payload = OrderedDict([('location',lat+','+lon),('radius',radius),('types',place_type),('key',freekey),('hasNextPage',True),('nextPage()',True),('pagetoken',token)])
	req = s.get(url,params=payload)
	reqdata = json.loads(req.text)
	print reqdata['status']
	write_in_file(reqdata)

		
#full_data = reqdata['results']	

#rf.write(str(full_data))
'''
for thtr in full_data:

	rf.write(json.dumps(thtr['name']))
	rf.write(json.dumps(thtr['geometry']))
	rf.write(json.dumps(thtr['types']))
	rf.write('\n')
'''