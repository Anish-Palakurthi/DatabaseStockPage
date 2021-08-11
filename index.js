const mysql = require("mysql2/promise");


connect();
async function connect() {

    try {
        const con = await mysql.createConnection({
            "host": "127.0.0.1",
            "user": "root",
            "password": "",
            "database": "test.db"

        });

        const result1 = await con.query(`SELECT * FROM stocks2 WHERE ticker = 'AAPL';`);
        console.table(result1[0]);

    }



    catch (err) {
        console.error(err);
    }

}
