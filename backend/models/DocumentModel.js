import db from "../config/db.js";

export const createDocument = async (companyId, documentName, documentPath) => {
  const [result] = await db.query(
    "INSERT INTO documents (company_id, document_name, document_path) VALUES (?, ?, ?)",
    [companyId, documentName, documentPath]
  );
  return result.insertId;
};

export const getDocumentsByCompany = async (companyId) => {
  const [rows] = await db.query(
    "SELECT * FROM documents WHERE company_id = ?",
    [companyId]
  );
  return rows;
};