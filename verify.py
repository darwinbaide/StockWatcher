import pprint
import yfinance as yf
import mysql1


def stockExists(stockName):
    try:# this function checks if the stock is found on te finance api
        stock = yf.Ticker(stockName)
        stock.info
        return True
    except:
        return False    

def tableExists(name):
    command="SELECT * FROM information_schema.tables WHERE table_schema = 'stocks' AND table_name = '"+name+"'LIMIT 1;"
    result=mysql1.runCommand(command)# sends out the command
    if(len(result) !=0):
        return True
    else:
        return False

