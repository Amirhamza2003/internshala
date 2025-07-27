# Aave V2 Wallet Credit Score Calculator

This project provides a Python script to calculate credit scores for Ethereum wallets based on their activity on the Aave V2 protocol. The script processes a JSON file containing user wallet transactions, aggregates deposit, borrow, and repay actions, and computes a credit score for each wallet.

## Features
- Reads a JSON file of Aave V2 user wallet transactions
- Aggregates net deposits, borrows, and repays per wallet
- Calculates a repayment rate and a credit score (0-1000) for each wallet
- Outputs a sorted list of wallets with their metrics and scores
- Optionally saves the results to a new JSON file

## Requirements
- Python 3.7 or higher

## Installation
No special installation is required. Just ensure you have Python 3.7+ installed on your system.

## Usage
1. **Prepare your input file:**
   - Place your transaction data in a file named `user-wallet-transactions.json` in the same directory as the script, or update the file path in the script as needed.
   - The JSON file should contain a list of transaction objects, each with the following structure:
     ```json
     [
       {
         "userWallet": "0x...",
         "action": "deposit" | "borrow" | "repay",
         "actionData": {
           "amount": "...",           // String or number, amount of the asset
           "assetPriceUSD": "..."     // String or number, price of the asset in USD
         }
       },
       ...
     ]
     ```

2. **Run the script:**
   - If using the provided `test.py` or `test.ipynb`, run it with Python:
     ```bash
     python test.py
     ```
   - Or open and run the notebook cells in `test.ipynb`.

3. **View the results:**
   - The script will print a summary of each wallet's net deposits, repays, borrows, repayment rate, and calculated credit score.
   - Optionally, you can uncomment the code at the end of the script to save the results to a JSON file (e.g., `aave_wallet_credit_scores.json`).

## Example Output
```
--- Aave V2 Wallet Credit Scores ---

Wallet: 0x04e9601bd84b0934af81475670ae5d0ab5e4b9b9
  Net Deposits: $6806413112249071616.00 USD
  Net Repays: $5404936638.92 USD
  Net Borrows: $128447246675.59 USD
  Repayment Rate: 4.04%
  Calculated Credit Score: 1000.00

Wallet: 0x04e96cdcfbcce8c972c5f976117784933e0cc6af
  Net Deposits: $1194690277867542272.00 USD
  Net Repays: $0.00 USD
  Net Borrows: $201844.88 USD
  Repayment Rate: 0.00%
  Calculated Credit Score: 1000.00

Wallet: 0x04ea240f764d8784d76485863ee5accf9e336f9e
  Net Deposits: $92703940.36 USD
  Net Repays: $63296233.58 USD
  Net Borrows: $63508732.06 USD
  Repayment Rate: 49.92%
  Calculated Credit Score: 1000.00
```

## Customization
- You can adjust the scoring logic in the `calculate_credit_score` function in the script to better fit your use case.
- To change the input or output file paths, edit the variables at the top of the script.

## Troubleshooting
- **File Not Found:** Ensure your `user-wallet-transactions.json` file is in the correct directory and the path in the script is correct.
- **Malformed JSON:** Make sure your JSON file is properly formatted. You can use online validators to check.
- **No Output:** If the script prints only the header and no wallet data, check that your JSON file contains valid transactions with the required fields.

## License
This project is provided for educational and research purposes. No warranty is provided. 