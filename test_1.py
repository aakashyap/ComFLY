
from selenium import webdriver
 #if windows
driver = webdriver.Chrome('C:/chromedriver.exe') 
#browser=webdriver.Firefox()
print("bc")
driver.get('https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/DEL_BOM_06-03-2018?contains=false&remove=')
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


#html=urlopen(url, context=ctx).read()
soup=BeautifulSoup(html_page,"html.parser")
tags=soup('span')
a=soup.find_all("span",{"class":"block city_name hidden-xs visible-stb ng-binding"})
b=soup.find_all("span",{"class":"block timeCa RobotoRegular ng-binding"})
c=soup.find_all("span",{"class":"block logo_name hidden-xs visible-stb light_gray flt_number_less600 ng-binding ng-scope"})
d=soup.find_all("span",{"class":"num ng-binding"})
#print(a)
#a=soup.findall('span')
handle=open('random.txt','w')
for i in a:
	#print(i.contents)
	handle.write("%s\n" % i.contents)
for i in b:
	#print(i.contents)
	handle.write("%s\n" % i.contents)
for i in c:
	#print(i.contents)
	handle.write("%s\n" % i.contents)
for i in d:
	#print(i.contents)
	handle.write("%s\n" % i.contents)

handle.close()
#for tag in tags:
	#if '' in tag.contents:
		#continue
	#print(tag.contents[0])

	