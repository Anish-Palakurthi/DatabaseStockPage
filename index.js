console.log("testing");
const mysql = require("mysql2/promise");
console.log("testing2")
var dates = ["test1"];
var prices1 = ["test2"];

var prices2 = ["test3"];

connect();

function returnDates() {
    console.log(dates)
    return dates;
}

function returnPrices1() {
    return prices1;
}

function returnPrices2() {
    return prices2;
}
returnDates();
returnPrices1();
returnPrices2();

async function connect() {

    try {
        const con = await mysql.createConnection({
            "host": "127.0.0.1",
            "user": "root",
            "password": "",
            "database": "test.db"

        });



        const q1 = await con.query(`SELECT * FROM stocks2 WHERE ticker = 'AAPL';`);
        var dateList = q1[0];




        console.table(dateList);


        for (var i = 0; i < dateList.length; i++) {

            var a = dateList[i].dateOfPrice;
            dates.push(a);

            var b = dateList[i].price;
            prices1.push(b);

            // console.log(dates[i]);
            //console.log(prices1[i]);

        }

        const q2 = await con.query(`SELECT * FROM stocks2 WHERE ticker = 'TSLA';`);
        var dateList = q2[0];


        for (var i = 0; i < dateList.length; i++) {

            var b = dateList[i].price;
            prices2.push(b);
            //console.log(prices2[i]);

        }

    }

    catch (err) {
        console.error(err);
    }



}



