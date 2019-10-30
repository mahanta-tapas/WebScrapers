from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pyvirtualdisplay import Display
from selenium.common.exceptions import NoSuchElementException

#driver = webdriver.Chrome('/home/tapas/Downloads/chromedriver')
#display = Display(visible=0, size=(800, 600))
#display.start()

'''
driver = webdriver.Firefox()
driver.get("http://www.tripadvisor.in/")
elem = driver.find_element_by_id("GEO_SCOPED_SEARCH_INPUT")
elem.send_keys("Hyderabad")
time.sleep(3)
elem.send_keys(Keys.RETURN)
time.sleep(3)
elem2 = driver.find_element_by_id("mainSearch")
elem2.send_keys("Things to do")
elem2.send_keys(Keys.RETURN)
btn = driver.find_element_by_id("SEARCH_BUTTON")
parent_tab = driver.current_window_handle	
btn.click()
time.sleep(5)
#print driver.title
url = driver.current_url
driver.close()
#driver = webdriver.Chrome('/home/tapas/Downloads/chromedriver')
driver = webdriver.Firefox()
driver.get(url)
'''
a = 0
padding =''
driver = webdriver.Firefox()
#driver = webdriver.Chrome('/home/tapas/Downloads/chromedriver')
while True:	
    url1 = 'http://www.tripadvisor.in/Attractions-g297586-Activities'
    url2 = '-Hyderabad_Telangana.html'
    url = url1+padding+url2
    driver.get(url)
    print url
    
    
    elem = driver.find_element_by_id("ATTR_CATEGORY_47")
    elem2 = elem.find_element_by_xpath("./a[@href]")
    elem2.click()
    
    parent_tab = driver.current_window_handle
    elem_list = driver.find_elements_by_class_name('element_wrap')
    for el in elem_list:
        print el
        elem2 = el.find_element_by_xpath(".//a[@href]")
        #print elem2.text
        elem2.click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[-1])
        #print "child is :"+str(driver.title)
        time.sleep(3)
        try:
        	elem = driver.find_element_by_class_name("info_wrapper")
    	except Exception:
    		continue
        elem3 = elem.find_element_by_xpath("./address")
        print elem3.text
        elem4 = driver.find_element_by_class_name("detail")
        detail_elem = elem4.find_element_by_xpath("./a[@href]")
        print detail_elem.text
        elem5 = driver.find_element_by_css_selector(".see_all,.fkASDF,.taLnk hvrIE6")
        print driver.current_url
        try:
        	elem6 = driver.find_element_by_class_name("hours")        
        	print elem6.text
        except NoSuchElementException:
        	pass	
        #elem5 = driver.find_element_by_link_text("See all hours")
        #print elem5.text
        elem5.click()
        
        print elem5.text
        #print driver.title
        try:
        	elem6 = driver.find_element_by_id("HOUR_OVERLAY_CONTENTS")
        	elem7 = elem6.find_element_by_xpath(".//div")
        	#print elem7
        	print elem7.text
        except NoSuchElementException:
        	pass
        	#print "element not found"	
        #time.sleep(100)
        driver.close()
        driver.switch_to_window(parent_tab)
        print "coming back to parent : "+ str(driver.title) 
        #print driver.current_url
    a = a+30
    padding = '-oa'+str(a)
    if len(elem_list)<30:
    	print "came here to break"
        break

#driver.switch_to_alert() 
#clk = driver.find_element_by_link_text("Places to Visit")
#clk.click()

#driver.find_element_by_id("ATTR_CATEGORY_47")
#clk2 = driver.find_element_by_xpath("a/@href")
#clk2.click()
