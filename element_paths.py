""" This is the list for easy editing if the site ever changes the structure  """

""" Page uses react and that is the only unique way to get the value after it changes """
#XPATH APPROACH
priceX="/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]"# the current price
volumeX="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[4]/td[2]/span"# total volume
closeX="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/span" # close yesterday
openX="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/span"# open today
rangeX="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]"# price range for today
volumeTX="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[5]/td[2]/span"# volume for 24 hours
changeX="/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[2]"










"""  

CoinMarketplace
priceX="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[1]/span[1]/span[1]"# the current price
volumeX="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[2]/div/span[1]"# total volume
closeX="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[17]/td/div[2]" # close yesterday
openX="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[17]/td/div[1]"# open today
highX="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[16]/td/div[1]"# price range for today
lowX="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[16]/td/div[2]"# price range for today
volumeTX="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/table/tbody/tr[19]/td"# volume for 24 hours
changeX="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[1]/span[2]"





#based off the react IDs
priceX="14"# the current price
volumeX="62"# total volume
closeX=".//td[@data-test='PREV_CLOSE-value']/span" # cloes yesterday
openX="21"# open today
rangeX="25"# price range for today
volumeTX="67"# volume for 24 hours
changeX="16"






"""