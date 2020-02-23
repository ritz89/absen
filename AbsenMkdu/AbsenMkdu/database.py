import mysql.connector

def getDbCursor():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
    )
    return mydb.cursor()

