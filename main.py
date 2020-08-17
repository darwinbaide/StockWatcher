import verify
import mysql1
import history
import current
import time,  pprint
""" This i the main controller for the scraper that gets the data every 15 minutes, will run the process on each item on the list file """




def runUpdate():    
    print("Start of Stock Watcher")
    # get all the stocks
    command="SELECT * FROM stocks.stocks where active1 =1;"# grab the list from DB
    lines =mysql1.runCommand(command)

    #loop through each one
    for row in lines:
        try:
            line= (row['symbol1'])# grabs the ysmbol name for the stock/crypto
            name=line.replace("-","_")# swap out the line for mysql DB name formatting
            if(verify.stockExists(line)== True):# verify that the symbol exists and gets a return from the yahoo finance api
                print("Starting Stock: "+line)# confirmtaiton it was found
            else:
                print("Stock "+line+" does not exist") 
                continue# continue and skip stock as it does not exist or is not recognized

            if(verify.tableExists(name)== False):# uses a simple table query to see if the stock is already in the system and creates and loads a table if its new
                newTable(name,line)# function with the creates
            if(row['cycle1']==1):
                current.runPeriodical(row['primary'])# runs the periodical stock parser
            else:
                print("dd")
        except:
            print("Error in getting stock infor for: "+line)

        
def newTable(name, line):
    print("Table for stock "+line+ " does not exist, creating new one" )
    command="CREATE TABLE `"+name+"` (  `primary` int(11) NOT NULL AUTO_INCREMENT,  `price` varchar(45) DEFAULT NULL,  `volume` varchar(45) DEFAULT NULL,  `close` varchar(45) DEFAULT NULL,  `open` varchar(45) DEFAULT NULL,  `volume(24)` varchar(45) DEFAULT NULL,  `timestamp` datetime DEFAULT current_timestamp(),`high` varchar(45) DEFAULT NULL,  `low` varchar(45) DEFAULT NULL,  `change` varchar(45) DEFAULT NULL, PRIMARY KEY (`primary`)) ENGINE=InnoDB AUTO_INCREMENT=4265 DEFAULT CHARSET=utf8mb4;"
    mysql1.runCommand(command)
    print("loading history for "+line)
    history.getHistory(line,name)
    print("Done")


def main():
            

    while True:
        runUpdate()
        print()
        print("Waiting 20 Minutes")
        print()
        time.sleep(1200)



if __name__ == '__main__':
    main()
    print("ran")
