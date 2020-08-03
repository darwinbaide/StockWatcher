import requests
from lxml import etree
import mysql1
import element_paths





def getPrice(stockName,tableName, website):
    page=requests.get(website)# get site
    print(website)
    tree = etree.HTML(page.text)


    SPrice=tree.find(".//span[@data-reactid='"+element_paths.priceX+"']")
    SVolume=tree.find(".//span[@data-reactid='"+element_paths.volumeX+"']")
    SClose=tree.find(element_paths.closeX)
    SOpen=tree.find(".//span[@data-reactid='"+element_paths.openX+"']")
    SRange=tree.find(".//td[@data-reactid='"+element_paths.rangeX+"']")
    SVolumeT=tree.find(".//span[@data-reactid='"+element_paths.volumeTX+"']")
    SChange=tree.find(".//span[@data-reactid='"+element_paths.changeX+"']")


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

    print(stockName+": "+price1)
       
    print("Price: "+price1)
    print("Volume: "+volume1)
    print("Close: "+close1)
    print("Open: "+open1)
    print("Volume(24H):"+ volumeT1)
    print("High: "+high1)
    print("Low: "+low1) 
    
    
    command="INSERT INTO `stocks`.`"+tableName+"`(`price`,`volume`,`close`,`open`,`volume(24)`,`timestamp`,`high`,`low`,`change`)VALUES('"+price1+"','"+volume1+"','"+close1+"','"+open1+"','"+volumeT1+"',now(),'"+high1+"','"+low1+"','"+change1+"');"
    #print(command)
    mysql1.runCommand(command)# sends out the command





#getPrice("ada","test","https://finance.yahoo.com/quote/ada-usd?p=ada-usd&.tsrc=fin-srch")