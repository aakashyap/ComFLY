import re
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe') 

driver.get('https://flight.yatra.com/air-search-ui/dom2/trigger?ADT=1&CHD=0&INF=0&class=Economy&destination=BOM&destinationCountry=IN&flexi=0&flight_depart_date=26/02/2018&noOfSegments=1&origin=DEL&originCountry=IN&source=fresco-home&type=O&version=1.15&viewName=normal')
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#serviceurl='https://www.makemytrip.com/'

#url='https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_06-03-2018?contains=false&remove='
html_page = driver.page_source
driver.quit()


soup=BeautifulSoup(html_page,"html.parser")
tags=soup('span')
#a=soup.find_all("span",{"class":"block city_name hidden-xs visible-stb ng-binding"})
airlin=soup.find_all("small",{"class":"fs-sm gray fl ml5 name carrier-name"})
dept_tim=soup.find_all("span",{"class":"time-color","ng-bind":"flt.dd"})
arr_tim=soup.find_all("span",{"class":"time-color","ng-bind":"flt.ad"})
flt_n=soup.find_all("small",{"class":"fs-10 ltr-gray fl ml5 nowrap"})
price=soup.find_all("del",{"class":"fs-sm lt-gray block ng-hide"})
journey=soup.find_all("small",{"class":"fs-10 ltr-gray block stop-tooltip three-dot"})

tempo=list()
finalpric=list()
airline=list()
dept_time=list()
arr_time=list()
flt_no=list()
finalprice=list()
journey_type=list()

#handle=open('random.txt','w')



for i in airlin:
	#handle.write("%s\n" % i.contents)
	tempo.append(i.contents)
for i in tempo:
	airline.append(i[0])
del tempo[:]


for i in dept_tim:
	#handle.write("%s\n" % i.contents)
	tempo.append(i.contents)
for i in tempo:
	dept_time.append(i[0])
del tempo[:]
#handle.write("******\n")

for i in arr_tim:
	#handle.write("%s\n" % i.contents)
	tempo.append(i.contents)
for i in tempo:
	arr_time.append(i[0])
del tempo[:]
#handle.write("******\n")


for i in flt_n:
	#handle.write("%s\n" % i.contents)
	tempo.append(i.contents)
for i in tempo:
	flt_no.append(i[0])
del tempo[:]


for i in price:
	t=str(i)
	temp=re.findall(r'[0-9][0-9,]+',t)
	finalpric.append(temp)
finalpric = [v for i, v in enumerate(finalpric) if i % 2 == 0]

for i in finalpric:
	#handle.write("%s\n" % i)
	tempo.append(i)
for i in tempo:
	finalprice.append(i[0])

for i in journey:
	#handle.write("%s\n" % i)
	tempo.append(i.contents)
for i in tempo:
	journey_type.append(i[0].rstrip())

print(airline)
print(dept_time)
print(arr_time)
print(flt_no)
print(finalprice)
print(journey_type)



	