import mysql.connector
import requests
import json
dates = []
closes = []
calls = ["http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2020-08-07&date_to=2020-09-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2020-09-02&date_to=2020-10-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2020-10-02&date_to=2020-11-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2020-11-02&date_to=2020-12-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2020-12-02&date_to=2021-01-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2021-01-02&date_to=2021-02-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2021-02-02&date_to=2021-03-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2021-03-02&date_to=2021-04-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2021-04-02&date_to=2021-05-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2021-05-02&date_to=2021-06-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2021-06-02&date_to=2021-07-01",
         "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2021-07-02&date_to=2021-08-05"]
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test.db')

# prepare a cursor object using cursor() method
cursor = cnx.cursor()


def slimDate(datesArray):
    dateList = []
    goodList = []
    for date in datesArray:
        dateList = ((date.split("T")))
        goodList.append(dateList[0])

    return goodList


for call in calls:
    api = requests.get(  # contacts API
        call
    )

    data = api.text
    parsed_json = json.loads(data)

    for x in range(len(parsed_json["data"])):
        date = (
            (parsed_json["data"])[x])["date"]
        dates.append(date)
        close = ((parsed_json["data"])[x])["close"]
        closes.append(close)


dates = slimDate(dates)
dates.reverse()

closes.reverse()

for close in closes:
    print(close)

cursor.execute("INSERT INTO stocks")
for i in range(len(closes)):
    cursor.execute(
        "ALTER TABLE stocks ADD `{dateColumn}` TEXT;".format(
            dateColumn=date))


cnx.close()
