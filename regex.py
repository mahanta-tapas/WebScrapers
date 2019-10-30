import re
import json
from bs4 import BeautifulSoup

strn = """<script type="text/javascript">
zomato = zomato || {};
zomato.DailyMenuMap = {};
zomato.DailyMenuMap.request_uri = "/bhubaneswar/restaurants?page=12";
zomato.DailyMenuMap.params = {"page":"12"};
zomato.DailyMenuMap.mapData = 
"1":{
"res_id":"2900125",
"lat":20.289916,
"lon":85.843249,
"rating":"0",
"rating_level":"level-0",
"result_page":1,
"establishment_name":"casual_dining",
"snippet":"<li class=\"resZS mbot0 pbot bb even  status1\" data-res_id=\"2900125\" data-position=\"12-1\">\n    <article class=\"search-result  first   pbot \">\n\n    <div class=\"row pb5 ptop0\">\n        <div class=\"col-m-12 search_result_info pos-relative\">\n            <div class=\"search-name clearfix\">\n                                <h3 class=\"top-res-box-name left\">\n                                            <a  class=\"result-title\"  href=\"https:\/\/www.zomato.com\/bhubaneswar\/the-black-pearl-restaurant-sahid-nagar-bhubaneshwar\" title=\"black pearl restaurant Restaurant, Sahid Nagar\" data-result-type=\"ResCard_Name\" >The Black Pearl Restaurant <\/a>\n                                                \n                                    <\/h3>\n                \n            <\/div>\n        \n                    \n            <div class=\"ln24 mt2 truncate zdark search-page-text\">\n                <a class=\"cblack\" href=\"https:\/\/www.zomato.com\/bhubaneswar\/sahid-nagar-restaurants\" title=\"Restaurants in Sahid Nagar\">Sahid Nagar<\/a>\n                                <span class=\"search-result-address\" title=\"B 63, Savitri Tower, Near Rupali Square, Sahid Nagar, Bhubaneswar\">&rsaquo; B 63, Savitri Tower, Near Rupali Square, Sahid...<\/span>\n                            <\/div>\n                            <div class=\"res-snippet-small-cuisine truncate search-page-text zdark\" title=\"<div class='res-snippet-small-cuisine truncate search-page-text' title='Casual Dining in Bhubaneswar'><a class='cblack' href='https:\/\/www.zomato.com\/bhubaneswar\/casual-dining'>Casual Dining<\/a> &rsaquo; North Indian, Chinese<\/div>\"><div class='res-snippet-small-cuisine truncate search-page-text' title='Casual Dining in Bhubaneswar'><a class='cblack' href='https:\/\/www.zomato.com\/bhubaneswar\/casual-dining'>Casual Dining<\/a> &rsaquo; North Indian, Chinese<\/div><\/div>\n                    <\/div>\n        <div class=\"col-m-4 search_result_rating ta-right pt5\">\n            <div class=\"search-result-stars ln24 clearfix\">\n                <div class=\"right\">\n                                        <div data-res-id=\"2900125\" title=\"Not rated\" class=\"res-rating-nf tooltip right rating-for-2900125 level-0\">\n                        -\n                    <\/div>\n                    <div class=\"clear\"><\/div>\n                    <div class=\"rating-rank right\">\n                        <!-- show the vote count only if there's a rating -->\n                                            <\/div>\n                                    <\/div>\n            <\/div>\n            <div class=\"clear\"><\/div>\n        <\/div>\n\n        <div class=\"col-s-16 zdark\">\n            <div class=\"search-page-text\">\n                                <div class=\"grey-text\"><span class=\"upc cblack sml\">Cost for 2<\/span> &rsaquo; Rs. 600 <\/div>\n                                        \n            <\/div>\n            <div class=\"clear\"><\/div>\n        \n                    \n                    \n            <div class=\"clear\"><\/div>\n        \n                    \n                    \n                    \n        <\/div>\n    <\/div>\n\n    \n\n    <div class=\"mtop0 row\">\n        <div class=\"col-m-11 search_result_links pos-relative\">\n                    <\/div>\n        \n        <div class=\"col-m-5 pl0 pr5 search_result_photos ta-right\">\n                        <div class=\"photosContainer\" data-res_id=\"2900125\" data-result-type=\"ResCard_thumbnails\">\n                <div class=\"search-result-gallery-container res-photo-thumbnails right\">\n                    <div class=\"res-photo-thumbnails right\">\n                                                <a href=\"#\" class=\"res-image-view res-image-view--thumbs mr5 mb5\"><img src=\"https:\/\/a.zmtcdn.com\/images\/photoback.png\" class=\"res-photo-thumbnail lazy\" data-original=\"https:\/\/b.zmtcdn.com\/data\/pictures\/5\/2900125\/fde2a8efcc99d395950d232f6ff9af47_200_thumb.jpg\" data-type=\"res\" data-photo_id=\"r_NTk2Mzk3MTAzNT\" data-index=\"0\" alt=\"The Black Pearl Restaurant, Sahid Nagar Pictures\"><\/a>\n                                                <a href=\"#\" class=\"res-image-view res-image-view--thumbs mr5 mb5\"><img src=\"https:\/\/a.zmtcdn.com\/images\/photoback.png\" class=\"res-photo-thumbnail lazy\" data-original=\"https:\/\/a.zmtcdn.com\/data\/pictures\/5\/2900125\/86b4d35aa42daf7853c7aea78f065049_200_thumb.jpg\" data-type=\"res\" data-photo_id=\"r_ODU2MTI0MzgxNT\" data-index=\"1\" alt=\"The Black Pearl Restaurant, Sahid Nagar Pictures\"><\/a>\n                                                                        <a href=\"#\" class=\"res-image-view res-image-view--thumbs mr5 mb5\"><div class=\"left-photo-count photomore user-info-thumbs-load-more res-photo-thumbnail\" data-type=\"res\" data-photo_id=\"r_ODE1NzU2NDY3NT\" >+1<\/div><\/a>\n                                                <div class=\"clear\"><\/div>\n                    <\/div>\n                <\/div>\n            <\/div>\n                    <\/div>\n    <\/div>\n\n    <div class=\"clear ieclear\"><\/div>\n\n        \n        \n    <\/article>\n\n    <\/li>\n"}
zomato.DailyMenuMap.center = {"lat":20.289916,"lon":85.843249};</script>"""
  
lat = re.findall('("lat":)(.*)(,)',strn,re.M|re.I)
lon = re.findall('("lon":)(.*)(,)',strn,re.M|re.I) 
#res = re.search('(zomato)(.*)',strn,re.M|re.I)

print (str(lat[1]).split(',')[1])
#soup = BeautifulSoup(strn)
#with open ("prettifile.html","w+") as pf:
	#pf.write(soup.prettify())
'''
res = strn.split(';',500)
#print (res[4])
print (" this is the second part \n")
print (res[5])
print (" this is the third part \n")
print (res[6])
print (" this is the fourth part \n")
print (res[7])
print (" this is the fifth part \n")
print (res[8])

final_res = res[4] + res[5] + res[6] + res[7] + res[8]

print ()
#final = result[1]
#print (final)
'''