import mysql from "mysql2/promise";

const db = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "Aug09Data@9k",
  database: "ea",
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});

export default db;
