import requests
from lxml import etree
import mysql1
import element_paths



website="https://finance.yahoo.com/quote/XRP-USD?p=XRP-USD"

page=requests.get(website)# get site
with open("test.html","w") as rr:
    rr.write(page.text)
    rr.close()
print(website)

tree = etree.HTML(page.text)


SPrice=tree.xpath(element_paths.priceX)[0]
SVolume=tree.xpath(element_paths.volumeX)[0]
SClose=tree.xpath(element_paths.closeX)[0]
SOpen=tree.xpath(element_paths.openX)[0]
SRange=tree.xpath(element_paths.rangeX)[0]
SVolumeT=tree.xpath(element_paths.volumeTX)[0]
SChange=tree.xpath(element_paths.changeX)[0]


try:
    price1=SPrice.text# will check that there is some response        
except:
    print("error Getting price")
try:
    volume1=SVolume.text# will check that there is some response        
except:
    print("error Getting volume")
try:
    close1=SClose.text# will check that there is some response        
except:
    print("error Getting close")
try:
    open1=SOpen.text# will check that there is some response        
except:
    print("error Getting open")
try:
    range1=SRange.text# will check that there is some response        
except:
    print("error Getting range")
try:
    volumeT1=SVolumeT.text# will check that there is some response        
except:
    print("error Getting volume(24)")
try:
    change1=SChange.text# will check that there is some response        
except:
    print("error Getting change")
low1=range1.split(" - ")[0]
high1=range1.split(" - ")[1]#split the range

    
print("Price: "+price1)
print("Volume: "+volume1)
print("Close: "+close1)
print("Open: "+open1)
print("Volume(24H):"+ volumeT1)
print("High: "+high1)
print("Low: "+low1)
print("Change: "+change1) 

