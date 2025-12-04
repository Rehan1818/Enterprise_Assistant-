import path from "path";
import fs from "fs";
import { spawn } from "child_process";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const uploadDocument = async (req, res) => {
  try {
    const userId = req.user.user_id;
    const companyId = req.user.company_id;

    if (!req.file) {
      return res.status(400).json({ message: "No file uploaded" });
    }

    const uploadedFilePath = req.file.path.replaceAll("\\", "/");

    // Resolve Python file path using __dirname
    const indexerPath = path.resolve(
      __dirname,
      "../../rag_backend/indexer.py"
    );

    // Check file exists
    const exists = fs.existsSync(indexerPath);

    console.log("CHECK FILE EXISTS:", exists);
    console.log("FINAL PY FILE PATH:", indexerPath);

    if (!exists) {
      return res.status(500).json({
        message: "Indexer Python file not found.",
        path: indexerPath,
      });
    }

    // Escape any special characters in file path
    const safeDocumentPath = path.resolve(uploadedFilePath);

    console.log("\n------------------------------------------------");
    console.log("RUNNING PYTHON INDEXER");
    console.log("PYTHON FILE →", indexerPath);
    console.log("DOCUMENT →", safeDocumentPath);
    console.log("COMPANY →", companyId);
    console.log("------------------------------------------------\n");

    const pythonProcess = spawn("python", [
      indexerPath,
      safeDocumentPath,
      String(companyId)
    ], {
      windowsHide: true
    });

    let pythonOutput = "";
    let pythonError = "";

    pythonProcess.stdout.on("data", (data) => {
      pythonOutput += data.toString();
    });

    pythonProcess.stderr.on("data", (data) => {
      pythonError += data.toString();
    });

    pythonProcess.on("close", (code) => {
      if (code !== 0) {
        console.error("PYTHON ERROR:", pythonError);
        return res.status(500).json({
          message: "Python indexer failed.",
          error: pythonError,
        });
      }

      try {
        const result = JSON.parse(pythonOutput);
        return res.status(200).json({
          message: "Document indexed successfully",
          result,
        });
      } catch (err) {
        console.error("JSON PARSE ERROR:", err);
        return res.status(500).json({
          message: "Invalid response from Python script",
          output: pythonOutput,
        });
      }
    });

  } catch (error) {
    console.error("UPLOAD ERROR:", error);
    return res.status(500).json({ message: "Server error", error });
  }
};
