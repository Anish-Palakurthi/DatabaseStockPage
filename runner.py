from flask import Flask, redirect, url_for, render_template, request
import requests  # needed for API pull
import json  # allows for json manipulation
import mysql.connector

# inputs for user


dates = []
closes1 = []
closes2 = []


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if (request.method == "POST"):

        stock1Prime = request.form["s1"]

        stock2Prime = request.form["s2"]

        return redirect(url_for("sqlconnect", stock1=stock1Prime, stock2=stock2Prime))

    else:

        return render_template("webpage.html")


@app.route("/sqlconnect/<string:stock1>/<string:stock2>", methods=["POST", "GET"])
def sqlconnect(stock1, stock2):

    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='test.db')

    cursor = cnx.cursor()

    message = "SELECT * FROM stocks2 WHERE ticker = '{s1}';".format(s1=stock1)
    cursor.execute(message)
    results = cursor.fetchall()
    for result in results:
        closes1.append(result[3])
        dates.append(result[2])

    message = "SELECT * FROM stocks2 WHERE ticker = '{s2}';".format(s2=stock2)
    cursor.execute(message)
    results = cursor.fetchall()
    for result in results:
        closes2.append(result[3])

    return(render_template("webpage.html", dateList=dates, stockList1=closes1, stockList2=closes2))


if __name__ == "__main__":
    app.run()
