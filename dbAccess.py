import mysql.connector
import requests
import json
dates = []
closes = []
'''
api = requests.get(  # contacts API
    "http://api.marketstack.com/v1/eod?access_key=469ed3642bddff1dee77e5b1332ce3b7&symbols=AAPL&date_from=2020-08-04"
)

data = api.text
parsed_json = json.loads(data)

for x in range(len(parsed_json["data"])):
    date = (
        (parsed_json["data"])[x])["date"]
    dates.append(date)
    close = ((parsed_json["data"])[x])["close"]
    closes.append(close)


def slimDate(datesArray):
    dateList = []
    goodList = []
    for date in datesArray:
        dateList = ((date.split("T")))
        goodList.append(dateList[0])

    return goodList


dates = slimDate(dates)
print(len(dates))
'''
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test.db')


# prepare a cursor object using cursor() method
cursor = cnx.cursor()

# execute SQL query using execute() method.

cursor.execute("ALTER TABLE stocks ADD Day3 TEXT;")

# Fetch a single row using fetchone() method.


cnx.close()
