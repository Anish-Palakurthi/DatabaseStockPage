import mysql.connector
import requests
import json
from datetime import date
dates = []
tempDates = []
tempCloses = []
closes = []


today = date.today()
print(today)


"http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=&date_to="


def slimDate(datesArray):
    dateList = []
    goodList = []
    for date in datesArray:
        dateList = ((date.split("T")))
        goodList.append(dateList[0])

    return goodList


def fillZeros(integer):
    sInt = str(integer)
    sInt = sInt.zfill(2)
    return(sInt)


def datesFromAPI(year, month, day):
    Year = int(year)
    Month = int(month)
    Day = int(day)
    tempYear = Year
    tempMonth = Month
    tempDay = Day
    tempDate = ("{year}-{month}-{day}".format(year=str(Year),
                month=fillZeros(Month), day=fillZeros(Day)))

    Date = ("{year}-{month}-{day}".format(year=str(Year),
                                          month=fillZeros(Month), day=fillZeros(Day)))
    for i in range(12):
        tempYear = Year  # 2020
        tempMonth = Month  # 08
        tempDay = Day  # 10
        dayBefore = Day + 1  # 11

        dayFrom = ("{tYear}-{tMonth}-{tDay}").format(tYear=tempYear,
                                                     tMonth=fillZeros(tempMonth), tDay=fillZeros(tempDay))

        if(Month == 12):
            Month = 1
            Year = Year + 1
        else:
            Month = Month + 1

        dayTo = ("{year}-{month}-{day}").format(year=Year,
                                                month=fillZeros(Month), day=fillZeros(dayBefore))
        callAPI(
            "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from={DF}&date_to={DT}".format(DF=dayFrom, DT=dayTo))


def callAPI(url):
    print(url)
    api = requests.get(  # contacts API
        url
    )

    data = api.text
    parsed_json = json.loads(data)
    for x in range(len(parsed_json["data"])):
        date = (
            (parsed_json["data"])[x])["date"]
        tempDates.append(date)
        close = ((parsed_json["data"])[x])["close"]
        tempCloses.append(close)
    tempDates.reverse()
    for date in tempDates:
        dates.append(date)
    tempCloses.reverse()
    for price in tempCloses:
        closes.append(price)


datesFromAPI("2020", "08", "10")

dates = slimDate(dates)
print(dates[0])
print(closes[0])


cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test.db')


# prepare a cursor object using cursor() method
cursor = cnx.cursor()


for i in range(len(dates)):
    message = (
        "INSERT INTO stocks2(ticker, dateOfPrice, price) VALUES ('AAPL', '{day}', {price});").format(day=dates[i], price=closes[i])
    cursor.execute(message)


cnx.close()
