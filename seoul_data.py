from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv
from pyvirtualdisplay import Display
import time
display = Display(visible=0, size=(800, 600))
display.start()
f = open("res_seoul264.csv",'wb')
a = 7860
ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
#12810
while a <=12810:
    url1 = 'http://www.tripadvisor.in/Restaurants-g294197-'
    a = a+30
    url2 = 'oa'+str(a)+'-Seoul.html#EATERY_LIST_CONTENTS'
    print 'page number :' + str((a/30)+1)
    url = url1+url2
    '''
    driver = webdriver.Firefox()
    driver.get("http://www.tripadvisor.in/")
    elem = driver.find_element_by_id("GEO_SCOPED_SEARCH_INPUT")
    elem.send_keys("Seoul")
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_id("mainSearch")
    elem.send_keys("Restaurants")
    elem.send_keys(Keys.RETURN)
    btn = driver.find_element_by_id("SEARCH_BUTTON")	
    btn.click()
    print driver.current_url
    '''
    
    '''
    s = requests.Session()
    response = s.get(url,headers=ua)
    f = response.content
    soup = BeautifulSoup((f))
    with open ("seoul_pretty","w") as f:
    f.write(soup.prettify().encode('utf-8'))
    '''
    driver = webdriver.Chrome('/home/tapas/Downloads/chromedriver')
    #driver = webdriver.Firefox()
    driver.get(url)
    parent_tab = driver.current_window_handle
    #elem = driver.find_element_by_link_text('Paris Baguette Gangnam Station Store')
    
    elem = driver.find_elements_by_class_name("shortSellDetails")
    for el in elem:
        elem2 = el.find_element_by_xpath(".//a[@href]")
        name = elem2.text
        print name
        #handle = driver.window_handles
        elem2.click()
        time.sleep(7)
        driver.switch_to_window(driver.window_handles[1])
        #tabelem = driver.find_element_by_css_selector("body")
        #tabelem.send_keys(Keys.CONTROL, Keys.PAGE_DOWN);
        #print driver.title
        elem3 = driver.find_element_by_class_name("threeColumnList")
        elem4 = elem3.find_element_by_xpath(".//div").text
        #print elem4
        
        res = elem4.split("\n")
        #print "len of res is "+ str(len(res))
        writer = csv.writer(f)

        try:    
            address = res[1].encode('utf-8')
        except ValueError:
            address =''
        except IndexError:
            address =''	
        try:		
            location = res[2].encode('utf-8')
        except ValueError:
            location = ''
        except IndexError:
            location = ''	
        try:	
            neighbourhood = res[3].encode('utf-8')
        except ValueError:
            neighbourhood = ''
        except IndexError:
            neighbourhood = ''		
        try:
            phone = res[4].encode('utf-8')
        except ValueError:
            phone = ''
        except IndexError:
            phone = ''		
						        
        try:
            if(len(res)==5):    
            	writer.writerow([name.encode('utf-8'),address.encode('utf-8'),location.encode('utf-8'),phone.encode('utf-8')])
            	#print name 
            elif(len(res)==4):
            	writer.writerow([name.encode('utf-8'),address.encode('utf-8'),location.encode('utf-8'),neighbourhood.encode('utf-8')])
            	#print location	
        except ValueError:
            if(len(res)==5):
            	writer.writerow([name,address,location,phone])
            elif(len(res)==4):
            	writer.writerow([name,address,location,neighbourhood])	
        	   	    
        #driver.back()

        #.get_attribute('innerHTML')
        
        driver.close()
        #tabelem = driver.find_element_by_css_selector("body")
        #tabelem.send_keys(Keys.CONTROL, Keys.PAGE_UP);
        driver.switch_to_window(parent_tab)
#driver.close()        
        #print driver.title
        #for el in elem:
        #elem2 = el.find_element_by_xpath(".//a[@href]")
        #print elem2.text
