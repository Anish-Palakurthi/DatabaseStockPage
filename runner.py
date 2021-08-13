from flask import Flask, redirect, url_for, render_template, request


# allows for json manipulation
import json


# connection from Python to MySQL
import mysql.connector


# arrays to store retrieved info from database
dates = []
closes1 = []
closes2 = []


app = Flask(__name__)

# designated as default page by single slash


@app.route("/", methods=["POST", "GET"])
def home():
    # form has action of post request
    if (request.method == "POST"):

        # inputs from form
        stock1 = request.form["s1"]

        stock2 = request.form["s2"]

        # connection created
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='test.db')

        # cursor acts as handle for MySQL commands
        cursor = cnx.cursor()

        # message is defined as the rows where stock1 is the ticker
        message = "SELECT * FROM stocks2 WHERE ticker = '{s1}';".format(
            s1=stock1)

        cursor.execute(message)

        # stores rows from SELECT line in results array
        results = cursor.fetchall()

        dates.clear()
        closes1.clear()
        closes2.clear()

        for result in results:

            # adds closing price and date for each day to arrays
            closes1.append(result[3])
            dates.append(result[2])

        message = "SELECT * FROM stocks2 WHERE ticker = '{s2}';".format(
            s2=stock2)
        cursor.execute(message)
        results = cursor.fetchall()
        for result in results:
            closes2.append(result[3])

        # returns template of original page with arrays as variables
        return(render_template("webpage.html", dateList=dates, stockList1=closes1, stockList2=closes2))

    else:
        # GET request comes from initial startup
        return render_template("webpage.html")


if __name__ == "__main__":
    app.run()
