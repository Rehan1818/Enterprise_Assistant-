import express from "express";
import cors from "cors";
import authRoutes from "./routes/authRoutes.js";
import documentsRoutes from "./routes/documentRoutes.js";

const app = express();
app.use(cors());
app.use(express.json());

app.use("/api/auth", authRoutes);
app.use("/api/documents", documentsRoutes);

app.get("/", (req, res) => {
    res.json({ message: "Backend API Working" });
});

app.listen(5000, () => console.log("Server running on port 5000"));
