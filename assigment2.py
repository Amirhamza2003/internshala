import fitz  # PyMuPDF
import pandas as pd
import random

# Step 1: Extract wallet addresses from PDF
pdf_path = r"C:\Users\Administrator\Desktop\internshala\Wallet id - Google Sheets.pdf"
doc = fitz.open(pdf_path)

wallets = []
for page in doc:
    text = page.get_text()
    for line in text.splitlines():
        if line.strip().startswith("0x") and len(line.strip()) == 42:
            wallets.append(line.strip())

print(f"Extracted {len(wallets)} wallet addresses.")

# Step 2: Fetch Compound protocol data (dummy data for demonstration)
def fetch_compound_data(wallet):
    # Replace this with real API calls to Compound or Covalent
    return {
        "wallet_id": wallet,
        "total_supplied": random.uniform(0, 10000),
        "total_borrowed": random.uniform(0, 10000),
        "total_repaid": random.uniform(0, 10000),
        "num_liquidations": random.randint(0, 5),
        "tenure_days": random.randint(10, 1000),
    }

features = [fetch_compound_data(wallet) for wallet in wallets]
df = pd.DataFrame(features)

# Step 3: Normalize features
for col in ["total_supplied", "total_borrowed", "total_repaid", "num_liquidations", "tenure_days"]:
    df[col + "_norm"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min() + 1e-9)

# Step 4: Calculate risk score (0-1000)
df["score"] = (
    0.3 * df["total_supplied_norm"] +
    0.2 * (1 - df["total_borrowed_norm"]) +
    0.3 * (df["total_repaid_norm"] / (df["total_borrowed_norm"] + 1e-9)) +
    0.1 * (1 - df["num_liquidations_norm"]) +
    0.1 * df["tenure_days_norm"]
) * 1000

# Step 5: Export to CSV
result = df[["wallet_id", "score"]]
result = result.copy()  # Add this line to avoid the warning
result["score"] = result["score"].astype(int)
result.to_csv("wallet_risk_scores.csv", index=False)

# Optional: Print a sample
print(result.head())