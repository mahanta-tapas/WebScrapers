from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv
from pyvirtualdisplay import Display
import time

url = "http://www.mapcoordinates.net/en"

driver = webdriver.Firefox()
driver.get(url)
elem  = driver.find_elements_by_css_selector("*");
print len(elem)
elem = driver.find_element_by_id('pac-input')
elem.send_keys("Rajaprasadamu,Masjid Banda,Hyderabad")
elem.send_keys(Keys.RETURN)

elem  = driver.find_elements_by_css_selector("*");
print len(elem)
'''
for el in elem:
	print el.tag_name
	print ('\n')
'''	
'''
elem2 = driver.find_element_by_class_name("options")
elem3 = driver.switch_to_frame(elem)
print elem3.text
'''