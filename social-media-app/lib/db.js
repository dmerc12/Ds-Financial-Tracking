import mysql from "mysql2/promise";

const mysql = require('mysql2/promise');

export async function db([ query, values = []]) {
    const dbConnection = await mysql.createConnection({
        user: process.env.USER,
        password: process.env.PASSWORD
    });

    try {
        const [results] = await dbConnection.execute(query, values);
        dbConnection.end();
        return results;
    } catch (error) {
        throw Error(error.message);
        return { error };
    }
}