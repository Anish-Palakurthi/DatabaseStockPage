# connector for Python->MySQL
import mysql.connector

# necessary for API call
import requests

# necessary to handle API return
import json

# imports assistance methods from other file
import helperMethods


# allows us to access current date and create date objects
from datetime import date
import datetime


yearAgo = datetime.datetime.today() - datetime.timedelta(days=365)
yearAgo = yearAgo.strftime(
    '%Y-%m-%d')  # format the date to ddmmyyyy
print(str(yearAgo))

dateListOne = yearAgo.split("-")

dates = []
tempDates = []
tempCloses = []
closes = []

boolean = yearAgo > today
print(boolean)


# connector to specific database
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test.db')


# cursor object allows us to run MySQL commands from Python script
cursor = cnx.cursor()

# determines if table exists and if it doesn't, creates appropriate table
message = "CREATE TABLE IF NOT EXISTS stocks2 (id  INT   NOT NULL    AUTO_INCREMENT PRIMARY KEY,ticker   TEXT    NOT NULL,dateOfPrice  TEXT NOT NULL,price INT);  "


# send command through to database
cursor.execute(message)

# saves changes to all users of database
cnx.commit()


# fetches date of last record from database
cursor.execute("SELECT*FROM stocks2 ORDER BY  id DESC LIMIT  1;")
lastRow = cursor.fetchone()
lastDate = (lastRow[2])
cnx.close()

dateListTwo = lastDate.split("-")

date1 = datetime.date(int(dateListOne[0]), int(
    dateListOne[1]), int(dateListOne[2]))
date2 = datetime.date(int(dateListTwo[0]), int(
    dateListTwo[1]), int(dateListTwo[2]))


'''




# manages ticking down month by month and then calling API each time
def prepareAPICall(year, month, day, company):
    Year = int(year)
    Month = int(month)
    Day = int(day)
    tempYear = Year
    tempMonth = Month
    tempDay = Day
    tempDate = ("{year}-{month}-{day}".format(year=str(Year),
                month=helperMethods.fillZeros(Month), day=helperMethods.fillZeros(Day)))

    Date = ("{year}-{month}-{day}".format(year=str(Year),
                                          month=helperMethods.fillZeros(Month), day=helperMethods.fillZeros(Day)))
    for i in range(12):
        tempYear = Year  #
        tempMonth = Month  #
        tempDay = Day  #
        dayBefore = Day + 1  #

        dayFrom = ("{tYear}-{tMonth}-{tDay}").format(tYear=tempYear,
                                                     tMonth=helperMethods.fillZeros(tempMonth), tDay=helperMethods.fillZeros(tempDay))

        if(Month == 12):
            Month = 1
            Year = Year + 1
        else:
            Month = Month + 1

        dayTo = ("{year}-{month}-{day}").format(year=Year,
                                                month=helperMethods.fillZeros(Month), day=helperMethods.fillZeros(dayBefore))

        date3 = dateTime.date(Year, Month, dayBefore)
        if date3 < today:
            callAPI(
                "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols={ticker}&date_from={DF}&date_to={DT}".format(DF=dayFrom, DT=dayTo, ticker=company))


def callAPI(url):
    print(url)
    api = requests.get(  # contacts API
        url
    )

    data = api.text
    parsed_json = json.loads(data)

    # adds dates of call to a temporaray dates array
    for x in range(len(parsed_json["data"])):
        date = (
            (parsed_json["data"])[x])["date"]
        tempDates.append(date)

        # adds closing prices of call to a temporaray closes array
        close = ((parsed_json["data"])[x])["close"]
        tempCloses.append(close)

    # reverses data to be in chronological order and then moves temp values to stored set
    tempDates.reverse()
    for date in tempDates:
        dates.append(date)

    tempCloses.reverse()
    for price in tempCloses:
        closes.append(price)

    tempCloses.clear()
    tempDates.clear()


if (isDateOneBefore is True):
    # hardcoded function call
    prepareAPICall(dateListTwo[0], dateListTwo[1], dateListTwo[2], "AMZN")
else:
    prepareAPICall(dateListOne[0], dateListOne[1], dateListOne[2], "AMZN")


dates = helperMethods.slimDate(dates)  # removes zeros


cnx = mysql.connector.connect(user='root', password='',  # connector from Python to MySQL
                              host='127.0.0.1',
                              database='test.db')


# prepare a cursor object using cursor() method
cursor = cnx.cursor()


def executeCursorMessage(company, date, closingPrice):
    message = ("INSERT INTO stocks2 (ticker, dateOfPrice, price) VALUES ('{ticker}', '{day}', {price});").format(
        day=dates[i], price=closes[i], ticker=company)
    cursor.execute(message)


for i in range(len(dates)):  # inserts data row for each closing price and corresponding day
    executeCursorMessage('AMZN', dates[i], closes[i])


cnx.commit()

cnx.close()  # shuts off cursor and connection
'''
