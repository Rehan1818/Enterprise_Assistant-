import express from "express";
import upload from "../middlewares/multer.js";
import { uploadDocument } from "../controllers/documentController.js";
import { verifyToken } from "../middlewares/authMiddleware.js";

const router = express.Router();

router.post(
  "/upload",
  verifyToken,
  upload.single("document"),   // <-- FIELD NAME MUST MATCH POSTMAN
  uploadDocument
);

router.get("/test", (req, res) => {
  res.send("Documents route working");
});

export default router;
