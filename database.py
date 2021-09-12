import mysql.connector

def getProfile(id):
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "libraryAssistant"
            )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM profiles WHERE studentId="+str(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    profile = None
    for row in myresult:
        profile = row
    mydb.close()
    return profile

def getRecordAndBook(id):
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "libraryAssistant"
            )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM records WHERE studentId="+str(id)
    mycursor.execute(sql)
    myrecord = mycursor.fetchall()
    record = None
    for row in myrecord:
        record = row
    bookQR = record[2]
    sql = "SELECT * FROM books WHERE bookQR="+bookQR
    mycursor.execute(sql)
    mybook = mycursor.fetchall()
    book = None
    for row in mybook:
        book = row
    mydb.close()
    return record, book


def insertRecords(id):
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "libraryAssistant"
            )
    mycursor = mydb.cursor()
    sql = "INSERT INTO RECORDS(bookName, bookQR, issueDate, returnDate) VALUES() WHERE studentId=" +str(id)
    mycursor.execute(sql)
