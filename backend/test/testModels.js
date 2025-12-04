import { createCompany } from "../models/CompanyModel.js";
import { createUser } from "../models/UserModel.js";
import { createDocument } from "../models/DocumentModel.js";

const test = async () => {
  console.log("Testing database...");

  const companyId = await createCompany("Test Company 5");
  console.log("Created Company ID:", companyId);

  const userId = await createUser(
    "Aleena only",
    "aleenakhan@test.com",
    "password123",
    "admin",
    companyId
  );
  console.log("Created User ID:", userId);

  const docId = await createDocument(
    companyId,
    "sample.pdf",
    `/uploads/${companyId}/sample.pdf`
  );
  console.log("Document ID:", docId);
};

test();
