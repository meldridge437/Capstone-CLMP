#!/usr/bin/python3
###################################################
#
#  Database Transaction Handler Script
#  Base Code from: https://realpython.com/python-mysql/
#  Developed by: Matthew Eldridge
#        Capstone Project 2020-2021
#
###################################################

######### Libraries #########
import sys
from mysql.connector import connect, Error
#from time import time

######### Global Vars #########

# connection parameters (move into locked files later)
HOST = "tecky.mynetgear.com"
USER = "capdb"
PASS = "capstone2020-1"
DB = "doorlock"

DBFieldsList = ["id","username","pin","last_updated","last_accessed"]

######### Functions #########

def connectMYSQL():
    try:
        connection = connect(host=HOST,user=USER,password=PASS,database=DB)
        return connection, connection.cursor()
    except Error as e:
        print(e)
        exit(1)

def findInDB(field, identifierField, identifier):
    query = "select {} from access where {} = {};".format(field,identifierField,identifier)
    connection, cursor = connectMYSQL()
    cursor.execute(query)
    results = cursor.fetchall()
    cleanUP(connection)
    return results


#def updateDBEntry()

def createNewDBEntry(fields, fieldsData):
    query = "insert into access {} values {};".format(fields,fieldsData)
    connection, cursor = connectMYSQL()
    cursor.execute(query)
    connection.commit()
    cleanUP(connection)
    return

def deleteDBEntry(databaseID):
    delete = "delete from access where id = {};".format(databaseID)
    connection, cursor = connectMYSQL()
    cursor.execute(delete)
    connection.commit()
    cleanUP(connection)
    return

def cleanUP(connection):
    connection.close()
    return

def argsToMYSQLFormat(argsList,areInputVals=False):
    argStr = "("
    for arg in argsList:
        if (str(arg).isdigit()):
            argStr += str(arg) + ","
        elif (areInputVals):
            argStr += "\"" + arg + "\","
        else:
            argStr += arg + ","
    fullArgStr = argStr[:-1] + ")"
    return fullArgStr


######### MAIN #########
fields = DBFieldsList[1:3]
data = ["matt",12345]

formattedFields = argsToMYSQLFormat(fields)
formattedData = argsToMYSQLFormat(data,True)

print("fields: " + formattedFields)
print("  data: " + formattedData)

#createNewDBEntry(formattedFields,formattedData)

results = findInDB("*","pin",12345)

print(results)

#deleteDBEntry(1)

#exit(0)
