import requests
from lxml import etree
import mysql1
import element_paths



def runPeriodical(index1):
    command="SELECT * FROM stocks.stocks where `primary` ="+str(index1)+";"
    lines =mysql1.runCommand(command)
    line=lines[0] # gets the first elemet as there should only be one unique Primary key
    site1=line['site1']
    stockName=line['name1']
    tableName=line['tableName1']
    

    page=requests.get(site1)# get site html as download from requests
    getPrice(page.text,stockName,tableName)# runs the stock price parser on the downloaded html

def getPrice(html4,stockName,tableName):
    page=html4
    tree = etree.HTML(page)

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

    print("    "+stockName+": "+price1)
    """ 
    print("Price: "+price1)
    print("Volume: "+volume1)
    print("Close: "+close1)
    print("Open: "+open1)
    print("Volume(24H):"+ volumeT1)
    print("High: "+high1)
    print("Low: "+low1)
    print("Change: "+change1) 
    """
    
    command="INSERT INTO `stocks`.`"+tableName+"`(`price`,`volume`,`close`,`open`,`volume(24)`,`timestamp`,`high`,`low`,`change`)VALUES('"+price1+"','"+volume1+"','"+close1+"','"+open1+"','"+volumeT1+"',now(),'"+high1+"','"+low1+"','"+change1+"');"
    #print(command)
    mysql1.runCommand(command)# sends out the command




if __name__ == '__main__':
    runPeriodical(3)
    print("ran")

