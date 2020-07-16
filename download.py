import pprint
import yfinance as yf

msft = yf.Ticker("ada-usd")



# get stock info
#info=msft.info
#pprint.pprint(info)
#get historical market data
hist = msft.history(period="max")
#pprint.pprint(hist)
#print(hist)
for i, j in hist.iterrows(): 
    print("I:"+str(i))
    print(j[1])
    print() 
"""

# show financials
msft.financials
msft.quarterly_financials
 """
