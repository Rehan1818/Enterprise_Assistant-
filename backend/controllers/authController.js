import db from "../config/db.js";
import fs from "fs";
import path from "path";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { console } from "inspector";

export const registerAdmin = async (req, res) => {
  try {
    const { company_name, admin_name, email, password } = req.body;

    if (!company_name || !admin_name || !email || !password) {
      return res.status(400).json({ message: "All fields are required" });
    }

    // STEP 1: Insert company in DB
    const [companyResult] = await db.execute(
      "INSERT INTO companies (company_name) VALUES (?)",
      [company_name]
    );

    const companyId = companyResult.insertId;

    // STEP 2: Create company folder in file system
    const companyFolder = path.join("data", "companies", String(companyId));

    if (!fs.existsSync(companyFolder)) {
      fs.mkdirSync(companyFolder, { recursive: true });
      fs.mkdirSync(path.join(companyFolder, "uploads"));
      fs.mkdirSync(path.join(companyFolder, "vector_store"));
    }

    // STEP 3: Insert admin user in DB
    const hashedPassword = await bcrypt.hash(password, 10);

await db.execute(
  "INSERT INTO users (full_name, email, password_hash, role, company_id) VALUES (?, ?, ?, ?, ?)",
  [admin_name, email, hashedPassword, "admin", companyId]
);

    return res.status(201).json({
      message: "Admin account and company created successfully",
      company_id: companyId,
      company_folder: companyFolder
    });

  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Server error", error: error.message });
  }
};

export const loginUser = async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password)
      return res.status(400).json({ message: "Email and password required" });

    // STEP 1 — Find user by email
    const [users] = await db.execute(
      "SELECT * FROM users WHERE email = ?",
      [email]
    );

    if (users.length === 0)
      return res.status(400).json({ message: "Invalid credentials" });

    const user = users[0];
    console.log("Fetched user:", user);

    // STEP 2 — Compare password with hashed password
    const passwordMatch = await bcrypt.compare(password, user.password_hash);
    if (!passwordMatch)
      return res.status(400).json({ message: "Invalid credentials" });

    // STEP 3 — Create JWT token
    const token = jwt.sign(
      {
        user_id: user.user_id,
        company_id: user.company_id,
        role: user.role,
      },
      "SECRET123",
      { expiresIn: "7d" }
    );

    // STEP 4 — Send response
    return res.status(200).json({
      message: "Login successful",
      user: {
        id: user.user_id,
        name: user.full_name,
        email: user.email,
        role: user.role,
        company_id: user.company_id,
      },
      token,
    });

  } catch (error) {
    console.log(error);
    return res.status(500).json({ message: "Server error", error: error.message });
  }
};
