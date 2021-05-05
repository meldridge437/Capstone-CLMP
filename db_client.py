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
#from termios import tcflush, TCIFLUSH
#from time import time

######### Global Vars #########

# connection parameters (move into locked files later)
HOST = "tecky.mynetgear.com"
USER = "capdb"
PASS = "capstone2020-1"
DB = "doorlock"

DBFieldsList = ["id","username","pin","fingertID"]

######### Functions #########

# IP Connect to DB
def connectMYSQL():
    try:
        # Pass needed creeeedentials 
        connection = connect(host=HOST,user=USER,password=PASS,database=DB)
        # return the whole and cursor() because this is needed for every interaction 
        return connection, connection.cursor()
    except Error as e:
        print(e)
        exit(1)

def findInDB(wantedFieldsList, KnownColumnList, KnownDataList, isUpdate=False):
    # Take Lists and Convert them to strings MySQL will take
    strArgs = formatFunctionArgs([wantedFieldsList,KnownColumnList,KnownDataList],[False,False,True])
    #Form the appropriate Query
    query = "select {} from access where {} = {};".format(strArgs[0],strArgs[1],strArgs[2])
    # Web Connect to DB
    connection, cursor = connectMYSQL()
    # Run the query
    cursor.execute(query)
    # Capture Results
    rawResults = cursor.fetchall()
    # Reformat MySQL Output to more Python Friendly List
    results = resultsToLists(rawResults)
    # Updating entries require finding first and the active session
    if (isUpdate):
        return connection, cursor, results
    else:
        # properly close connection
        cleanUP(connection)
        return results


def updateDBEntry(KnownColumnList, KnownDataList, setColumnsList, DataToBeSetList):
    # Get the id # of the entry to be updated
    connection, cursor, foundResults = findInDB(["id"], KnownColumnList, KnownDataList, True)
    # Take Lists and Convert them to strings MySQL will Take
    strArgs = formatFunctionArgs([setColumnsList, DataToBeSetList],[False,True],True)
    # Form the query
    query = "update access set {} where id = {};".format(strArgs,foundResults[0])
    # Run the Query
    cursor.execute(query)
    # Commit the changes to the DB
    connection.commit()
    # Properly close the connection
    cleanUP(connection)
    return 


def createNewDBEntry(fieldsList, fieldsData):
    # Take Lists and Convert them to strings MySQL will take
    strArgs = formatFunctionArgs([fieldsList, fieldsData],[False,True])
    # Form the Query
    query = "insert into access ({}) values({});".format(strArgs[0],strArgs[1])
    # Web Connect to DB
    connection, cursor = connectMYSQL()
    # Run the Query
    cursor.execute(query)
    # Commit any changes to the DB
    connection.commit()
    # Properly close connection
    cleanUP(connection)
    return

def deleteDBEntry(databaseID):
    # Form the query
    delete = "delete from access where id = {};".format(databaseID)
    # Web Connect to DB
    connection, cursor = connectMYSQL()
    # Run the Query
    cursor.execute(delete)
    # Commit the changes to the DB
    connection.commit()
    # Properly close the connection
    cleanUP(connection)
    return

def cleanUP(connection):
    connection.close()
    #tcflush(sys.stdin,TCIFLUSH)
    return

# MySQL is Very Picky. This gets Python List of args to 
# the format MySQL will accept
# NOTE: MySQL handles strings a little different 
#       depending if they are the name of a column vs data
def argsToMYSQLFormat(argsList,areInputVals=False):
    # MySQL requires (,,,) for lists 
    # MySQL doesn't like (*) so override if statement
    if (argsList == "*"):
        return argsList
    if (len(argsList) == 1):
        return (str(argsList[0]),"\""+str(argsList[0])+"\"")[areInputVals]
    argStr = ""
    for arg in argsList:
        # Numbers can be directly added
        if (str(arg).isdigit()):
            argStr += str(arg) + ","
        # Strings to be stored within the database need "" around them
        elif (areInputVals):
            argStr += "\"" + arg + "\","
        # Strings that are names of table columns are directly added
        else:
            argStr += arg + ","
    fullArgStr = argStr[:-1] 
    return fullArgStr

# To Handle 2D Arrays that need to be formatted with different constraints
# Mainly Called inside the above fuctions
# NOTE: DO NOT PRE-FORMAT LISTS TO BE PASSED TO THE OTHER FUNCTIONS
def formatFunctionArgs(argsList, areInputsList, isUpdate=False):
    formattedArgs = []
    if (isUpdate):
        setsOfArgs = []
        for col,dat in zip(argsList[0],argsList[1]):
            setsOfArgs.append(str(col) + "=" + argsToMYSQLFormat([dat],True))
        return argsToMYSQLFormat(setsOfArgs)
    i = 0
    # Run through each list that is to be formatted
    for arg in argsList:
        formattedArgs.append(argsToMYSQLFormat(arg,areInputsList[i]))
        i += 1
    # return list of strings for querys
    return formattedArgs

# MySQL returns a python List with 1 element that is a multi-tuple
def resultsToLists(mysqlOutput):
    parts = []
    # Get the Data out from the original list
    try:
        multiPart = mysqlOutput[0]
    except:
        return parts
    # place each element directly into a list
    for part in multiPart:
        parts.append(part)
    # Return Python Friendly MySQL Results
    return parts


