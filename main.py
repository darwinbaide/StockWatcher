import verify
import mysql1
import history
import current
import time,  pprint, sys
import psutil
from subprocess import Popen, PIPE
import subprocess, os
""" This is the main controller for the scraper that gets the data every 15 minutes, will run the process on each item on the list file """




def runCycle():    
    print("Start of Stock Watcher")
    # get all the stocks
    command="SELECT * FROM stocks.stocks where active1=1 and cycle1 =2;"# grab the list from DB
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
            
            current.runPeriodical(row['primary'])# runs the periodical stock parser
            
        except:
            print("Error in getting stock infor for: "+line)

        

def runActive():
    print("starting Active")
    # get all the stocks
    command="SELECT * FROM stocks.stocks where active1=1 and cycle1 =1;"# grab the list from DB
    lines =mysql1.runCommand(command)# gets the lines for the actively run stocks

    closeInactive(lines)
    

    for line in lines:
        #print("cycle through active")
        confirmActive(line['primary'])# start up the active ones

def confirmActive(index1):
    #print("toggle the active ones on if not already")
    check1=0
    for p in psutil.process_iter():# iterate through currently running to see if its already running
        
        if( ('python' in p.name())  ):
            if(len(p.cmdline())!=3):# if it doesnt have three parts then skip
                continue
            if(("runConstant" in p.cmdline()[1]) and (str(index1) in str(p.cmdline()[2]))):    # will check that it has the correct file and the wanted index to scrape
               check1=1
    if(check1==0):
        print("starting: "+str(index1))# if it wasnt already found, then start the process
        
        if("nt" is os.name):    
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            DETACHED_PROCESS = 0x00000008
            p = subprocess.Popen(['python3', 'C:\\xampp\\htdocs\\dashboard\\StockWatcher\\runConstant.py ',str(index1)], stdin=PIPE, stdout=PIPE, stderr=PIPE,  creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
        else:
            p = subprocess.Popen(['python3', '/var/www/html/darwin/StockWatcher/runConstant.py',str(index1)],shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

        
        print ("Started Script up with PID: "+str(p.pid))
        
    #else:
    #    print("already running: "+str(index1))# it was already running so ignore  and continue




def closeInactive(lines):
    for p in psutil.process_iter():
        
        if(('python' in p.name()) ):
            if(len(p.cmdline())!=3):# if it doesnt have three parts then skip
                continue
            if("runConstant" in p.cmdline()[1]):    
                #print("\n\n\n")
                number1=p.cmdline()[2] 
                #print (p.cmdline()[2])
                print("Found: "+str(number1))
                if not (checkIt(lines,number1)):
                    print('Killing: '+str(number1))# if not found on the list that should be alive, then kill it
                    p = psutil.Process(p.pid)
                    p.terminate()  #or p.kill()




def checkIt(lines, index1):
    for h in lines:
        #print(h['primary'])
        if (str(h['primary']) == str(index1)):
            return True
    return False

def newTable(name, line):
    print("Table for stock "+line+ " does not exist, creating new one" )
    command="CREATE TABLE `"+name+"` (  `primary` int(11) NOT NULL AUTO_INCREMENT,  `price` varchar(45) DEFAULT NULL,  `volume` varchar(45) DEFAULT NULL,  `close` varchar(45) DEFAULT NULL,  `open` varchar(45) DEFAULT NULL,  `volume(24)` varchar(45) DEFAULT NULL,  `timestamp` datetime DEFAULT current_timestamp(),`high` varchar(45) DEFAULT NULL,  `low` varchar(45) DEFAULT NULL,  `change` varchar(45) DEFAULT NULL, PRIMARY KEY (`primary`)) ENGINE=InnoDB AUTO_INCREMENT=4265 DEFAULT CHARSET=utf8mb4;"
    mysql1.runCommand(command)
    print("loading history for "+line)
    history.getHistory(line,name)
    print("Done")


def main():
            
    countCycle=0
    while True:
        if(countCycle==4):
            runCycle() # will update the ones that are cycled
            runActive()# will check the ones that are actively checked
            countCycle=0#reset the wait
        else:
            runActive()# will check the actively watched more often and the cycled ones every 20 minutes
        print()
        print("Waiting 5 Minutes to check")
        print()
        time.sleep(3)
        countCycle=countCycle+1



if __name__ == '__main__':
    main()
    #runActive()
    #confirmActive(1)
    print("ran")
