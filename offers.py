from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='https://www.makemytrip.com/daily-deals/'

html=urlopen(url, context=ctx).read()
soup=BeautifulSoup(html,"html.parser")
a=soup.find_all("h3")
print(a)