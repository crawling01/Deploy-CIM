// app/templates/db.js
const mysql = require('mysql2/promise'); // Gunakan versi promise

const dbConfig = {
  host: process.env.DB_HOST || 'db',
  user: process.env.DB_USER || 'deploy',
  password: process.env.DB_PASSWORD || 'N4s1r4w0n!',
  database: process.env.DB_NAME || 'CIM',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
};

// Buat connection pool
const pool = mysql.createPool(dbConfig);

// Test koneksi saat pertama kali
pool.getConnection()
  .then(conn => {
    console.log('Connected to MySQL database');
    conn.release();
  })
  .catch(err => {
    console.error('Database connection failed:', err);
  });

module.exports = pool;