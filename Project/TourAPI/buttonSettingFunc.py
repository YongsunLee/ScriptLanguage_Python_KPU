import urllib.request
import xml.etree.ElementTree as ET

def OkbuttonSettingFunc(contentTypeId, cat3, areaCode, sigunguCode, ListView):
    nameList = []
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&contentTypeId="+str(contentTypeId)+"&areaCode="+str(areaCode)+"&sigunguCode="+str(sigunguCode)+"&cat1=A01&cat2=A0101&cat3="+str(cat3)+"&listYN=Y&MobileOS=ETC&MobileApp=AppTesting&arrange=A&numOfRows=20&pageNo=1"

    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("item")
    for i in iter:
        name = i.find("title")
        nameList.append(name.text)

    print(contentTypeId)
    print(cat3)
    print(areaCode)
    print(sigunguCode)

    #ListView.setModel(nameList)

    nameList.clear()

