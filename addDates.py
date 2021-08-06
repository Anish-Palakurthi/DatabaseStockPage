import mysql.connector
import requests
import json
dates = []
closes = []

"http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=&date_to="


def slimDate(datesArray):
    dateList = []
    goodList = []
    for date in datesArray:
        dateList = ((date.split("T")))
        goodList.append(dateList[0])

    return goodList


def datesFromAPI(year, month, day):
    Year = int(year)
    Month = int(month)
    Day = int(day)
    tempYear = Year
    tempMonth = Month
    tempDay = Day
    tempDate = ("{year}-{month}-{day}".format(year=str(Year),
                month=str(Month.zfill(2)), day=str(Day.zfill(2))))
    Date = ("{year}-{month}-{day}".format(year=str(Year),
                                          month=str(Month.zfill(2)), day=str(Day.zfill(2))))
    for i in range(12):
        tempYear = Year
        tempMonth = Month
        tempDay = Day
        if(Month == 1):
            Month = 12
            Year = Year - 1
        else:
            Month = Month - 1
            tempDate = ("{tYear}-{tMonth}-{tDay}").format(tYear=tempYear,
                                                          tMonth=tempMonth.zfill(2), tDay=tempDay.zfill(2))
            Date = ("{year}-{month}-{day}").format(year=Year,
                                                   month=Month.zfill(2), day=Day.zfill(2))
            callAPI(
                "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from={DF}&date_to={DT}".format(DF=Date, DT=tempDate))


def callAPI(url):
    print("url")
    print(url)
    api = requests.get(  # contacts API
        url
    )

    data = api.text
    parsed_json = json.loads(data)
    print(data)


datesFromAPI("2020", "08", "10")

'''
    for x in range(len(parsed_json["data"])):
        date = (
            (parsed_json["data"])[x])["date"]
        dates.append(date)
        close = ((parsed_json["data"])[x])["close"]
        closes.append(close)


datesFromAPI("2020", "08", "10")
dates = slimDate(dates)
dates.reverse()
closes.reverse()

for date in dates:
    print(date)

for close in closes:
    print(close)



cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test.db')


# prepare a cursor object using cursor() method
cursor = cnx.cursor()

for date in dates:
    cursor.execute(
        "ALTER TABLE stocks ADD `{dateColumn}` TEXT;".format(
            dateColumn=date))


cnx.close()

'''
