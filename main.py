import verify
import mysql1
import history
import current
import time
""" This i the main controller for the scraper that gets the data every 15 minutes, will run the process on each item on the list file """




def runUpdate():    
    print("Start of Stock Watcher")
    # get all the stocks
    with open("stocks.txt","r") as rb:
        lines=rb.readlines()# readlines of all the stocks
        rb.close()


    #loop through each one
    for line in lines:
        try:
                
            line=line.replace("\n","")# text file has new lines
            if line=="":# skip any empty lines
                continue
            name=line.replace("-","_")# swap out the line for mysql DB

            if(verify.stockExists(line)== True):
                print("Starting Stock: "+line)
            else:
                print("Stock "+line+" does not exist") 
                continue

            
            if(verify.tableExists(name)== False):
                print("Table for stock "+line+ " does not exist, creating new one" )
                command="CREATE TABLE `"+name+"` (  `primary` int(11) NOT NULL AUTO_INCREMENT,  `price` varchar(45) DEFAULT NULL,  `volume` varchar(45) DEFAULT NULL,  `close` varchar(45) DEFAULT NULL,  `open` varchar(45) DEFAULT NULL,  `volume(24)` varchar(45) DEFAULT NULL,  `timestamp` datetime DEFAULT current_timestamp(),`high` varchar(45) DEFAULT NULL,  `low` varchar(45) DEFAULT NULL,  `change` varchar(45) DEFAULT NULL, PRIMARY KEY (`primary`)) ENGINE=InnoDB AUTO_INCREMENT=4265 DEFAULT CHARSET=utf8mb4;"
                mysql1.runCommand(command)
                print("loading history for "+line)
                history.getHistory(line,name)
                print("Done")

            website="https://finance.yahoo.com/quote/"+line+"?p="+line+"&.tsrc=fin-srch"
            current.getPrice(line,name, website)

        except:
            print("Error in getting stock infor for: "+line)

        

while True:
    runUpdate()
    print()
    print("Waiting 15 Minutes")
    print()
    time.sleep(900)