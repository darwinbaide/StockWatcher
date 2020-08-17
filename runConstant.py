import sys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from lxml import etree
import mysql1
import element_paths, current



def loadMain(index1):# will take the index of the stock to run
    
    command="SELECT * FROM stocks.stocks where `primary` ="+str(index1)+";"# rabs the information for that index
    lines =mysql1.runCommand(command)
    line=lines[0] # grabs the first line as its tthe only one
    site1=line['site1'] # the url to run


    opts = Options()
    opts.headless = True # tells the script to run chrome headless
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])# dont output the console errors for the webpage
    browser = Chrome(options=opts)# sets the options to the browser object
    browser.get(site1) # opens the given url
    browser.execute_script("return document.documentElement.innerHTML;")# will wait for page to load
    root = browser.find_element_by_xpath('/*')# find root
    text=root.get_attribute('innerHTML')# get inner html of root and whole document
    time.sleep(5)# wait a little before starting to get the data

    count=0 # counter to test how many runs its had
    
    while(count<2):   
        text=root.get_attribute('innerHTML')# get inner html of root and whole document
        current.getPrice(text,line['name1'],line['tableName1'])# run the function to parse the data from the html extracted
        time.sleep(5) # wait 5 seconds before grabbing it again
        count=count+1 # increase the4 counter

    
    
    browser.quit()# at the end of script, kill the browser and the controller


def cycle():
    print("here")
    while(True):
        print("1")
        time.sleep(2)

if __name__ == '__main__':
    #loadMain(2)
    cycle()
    print("ran")
