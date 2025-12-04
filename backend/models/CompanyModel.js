import db from "../config/db.js";

export const createCompany = async (name) => {
  const [result] = await db.query(
    "INSERT INTO companies (company_name) VALUES (?)",
    [name]
  );
  return result.insertId;  // return company_id
};

export const getCompanyById = async (companyId) => {
  const [rows] = await db.query(
    "SELECT * FROM companies WHERE company_id = ?",
    [companyId]
  );
  return rows[0];
};
