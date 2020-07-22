import pprint
import yfinance as yf
import mysql1



def getHistory(stockName, tableName):    
    stock = yf.Ticker(stockName)
    hist = stock.history(period="max")# gets all available history
    for i, j in hist.iterrows(): 
        """ # for debugging
        print("Date:"+str(i))
        print("Open: "+str(j[0]))
        print("Close: "+str(j[3]))
        print("High: "+str(j[1]))
        print("Low: "+str(j[2]))
        print("Volume: "+str(j[4]))
        print() 
        """
        date1= str(i)
        open1= str(j[0])
        close1=str(j[3])
        high1=str(j[1])
        low1=str(j[2])
        volume1=str(j[4])
        # gets the six things i want for each row
        command="INSERT INTO `stocks`.`"+tableName+"`(`price`,`volume`,`close`,`open`,`volume(24)`,`timestamp`,`high`,`low`)VALUES('','"+volume1+"','"+close1+"','"+open1+"','','"+date1+"','"+high1+"','"+low1+"');"

        mysql1.runCommand(command)# sends out the command
