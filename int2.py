import re
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('https://www.makemytrip.com/air/search?tripType=O&itinerary=DEL-SYD-D-16Apr2018&paxType=A-1&cabinClass=E')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#serviceurl='https://www.makemytrip.com/'

#url='https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_06-03-2018?contains=false&remove='
html_page_yatra = driver.page_source
driver.quit()

tempo=list()
airline_mmt=list()

soup=BeautifulSoup(html_page_yatra,"html.parser")
airlinmmt=soup.find_all("span",{"mt-id":"an"})
for i in airlinmmt:
	#handle.write("%s\n" % i.contents)
	tempo.append(i.contents)
for i in tempo:
	airline_mmt.append(i[0].strip())
print(airline_mmt)



