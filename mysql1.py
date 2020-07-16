import pymysql
import json
from datetime import datetime




def runCommand(command):
    dbconn = connect()
    co = dbconn.cursor()
    co.execute(command)
    s = list()
    for result in co.fetchall():
        s.append(result)
    dbconn.commit ()
    dbconn.close()
    return s


def connect():
    try:
        mydb = pymysql.connect(host="127.0.0.1",
                               user="darwin",
                               password="Db12345678",
                               db="stocks",
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        return mydb
    except:
        print("error connecting to database")
        return None
