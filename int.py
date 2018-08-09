import re
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe') 

driver.get('https://flight.yatra.com/air-search-ui/int2/trigger?ADT=1&CHD=0&INF=0&class=Economy&destination=SYD&destinationCountry=AU&flexi=0&flight_depart_date=16/04/2018&hb=0&noOfSegments=1&origin=DEL&originCountry=IN&type=O&unique=997350426044&version=1.1&viewName=normal')
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
airline=list()
dept_time=list()
arr_time=list()
finalpric=list()
finalprice=list()
journey_type=list()
journey_duration=list()
journey_through=list()

soup=BeautifulSoup(html_page_yatra,"html.parser")
airlin=soup.find_all("p",{"class":"full airline-name"})
for i in airlin:
	#handle.write("%s\n" % i.contents)
	tempo.append(i.contents)
for i in tempo:
	airline.append(i[0].strip())
del tempo[:]
print(airline)

random=list()
rand_tim=soup.find_all("p",{"class":"full fm-lsb time-detail"})
for i in rand_tim:
	tempo.append(i.contents)
for i in tempo:
	random.append(i[0].strip())
del tempo[:]
dept_time = [v for i, v in enumerate(random) if i % 2 == 0]
arr_time=[v for i, v in enumerate(random) if i % 2 != 0]
print(dept_time)
print(arr_time)


price=soup.find_all("p",{"class":"fl price-value fm-lb"})
for i in price:
	t=str(i)
	temp=re.findall(r'[0-9][0-9,]+',t)
	finalpric.append(temp)
for i in finalpric:
	for j in i:
		if "," in j:
			finalprice.append(j)
print(finalprice)
str=""
journey=soup.find_all("p",{"class":"full fs-11 ltr-gray three-dot mt2 fly-stop"})
for i in journey:
	tempo.append(i.contents)
for i in tempo:
	journey_type.append(i[0].strip())
#for i in journey_type:
	#var=i.split()
	#journey_through.append(var[0]+var[1]+var[2])

print(journey_type)
del tempo[:]

time=soup.find_all("p",{"class":"full duration"})
for i in time:
	tempo.append(i.contents)
for i in tempo:
	journey_duration.append(i[0].strip())
print(journey_duration)


