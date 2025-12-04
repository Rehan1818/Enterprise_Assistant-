import db from "../config/db.js";

export const createUser = async (name, email, password, role, companyId) => {
  const [result] = await db.query(
    "INSERT INTO users (full_name, email, password_hash, role, company_id) VALUES (?, ?, ?, ?, ?)",
    [name, email, password, role, companyId]
  );
  return result.insertId;
};

export const getUserByEmail = async (email) => {
  const [rows] = await db.query(
    "SELECT * FROM users WHERE email = ?",
    [email]
  );
  return rows[0];
};
