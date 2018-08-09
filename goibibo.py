import urllib.request, urllib.parse, urllib.error
import json
url="http://developer.goibibo.com/api/search/?app_id=9395d693&app_key=e3dd1bc5ccffc93928fbe7d046f168e2&format=json&source=DEL&destination=BOM&dateofdeparture=20180305&seatingclass=E&adults=1&children=0&infants=0&counter=100"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
try:
	js = json.loads(data)
except:
    js = None
#if not js or 'status' not in js or js['status'] != 'OK':
	#print('==== Failure To Retrieve ====')
	#print(data)
	#continue


airlin=list()
flt_no=list()
dept_time=list()
arr_time=list()
finalprice=list()
journey_type=list()
journey_duration=list()
journey_through=list()
#print(json.dumps(js, indent=4))
temp=js["data"]["onwardflights"]
for item in temp:
	airlin.append(item["airline"])
	flt_no.append(item["carrierid"]+"-"+item["flightcode"])
	dept_time.append(item["deptime"])
	arr_time.append(item["arrtime"])
	journey_duration.append(item["duration"])
	finalprice.append(item["fare"]["grossamount"])
#print(airlin)
#print(flt_no)
#print(dept_time)
#print(arr_time)
#print(journey_duration)
#print(finalprice)
