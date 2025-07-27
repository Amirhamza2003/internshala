# Wallet Risk Scoring – Methodology Report

## Data Collection Method

- **Source:** Wallet addresses were extracted from a provided PDF using PyMuPDF.
- **Protocol Data:** For each wallet, protocol activity features (total supplied, borrowed, repaid, liquidations, tenure) were simulated for demonstration. In a production setting, these would be fetched from Compound V2/V3 APIs, Covalent, or similar blockchain data providers.

## Feature Selection Rationale

- **Total Supplied:** Indicates the amount a wallet has contributed as collateral, reflecting positive protocol participation.
- **Total Borrowed:** High borrowing may indicate higher risk if not matched by repayments.
- **Total Repaid:** Measures responsible borrowing behavior.
- **Number of Liquidations:** More liquidations suggest riskier or failed positions.
- **Tenure (Days):** Longer protocol engagement suggests reliability and experience.

## Scoring Method

- **Normalization:** Each feature is normalized to a 0–1 scale to ensure comparability.
- **Weighted Sum:** Features are combined using a weighted sum:
    - 30% Total Supplied (normalized)
    - 20% (1 - Total Borrowed, normalized)
    - 30% Repayment Ratio (repaid/borrowed, normalized)
    - 10% (1 - Number of Liquidations, normalized)
    - 10% Tenure (normalized)
- **Scaling:** The final score is scaled to a 0–1000 range and rounded to the nearest integer.

## Justification of Risk Indicators

- **Supplied/Collateral:** More collateral generally means lower risk.
- **Borrowed:** Excessive borrowing without repayment increases risk.
- **Repayment Ratio:** High repayment ratio is a strong indicator of low risk.
- **Liquidations:** Frequent liquidations are a red flag for risky behavior.
- **Tenure:** Longer tenure implies more experience and trustworthiness.

## Output

- The final output is a CSV file with columns: `wallet_id` and `score`, where each wallet is assigned a risk score between 0 and 1000.

---

*This approach is modular and can be easily extended to real on-chain data and additional features as needed.*