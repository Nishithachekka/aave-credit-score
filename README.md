# Aave V2 Wallet Credit Scoring

This project generates a credit score for each wallet interacting with the Aave V2 protocol based on historical transaction behavior. The score ranges from 0 to 1000 — with higher scores indicating responsible, reliable usage, and lower scores flagging potentially risky or exploitative activity.

---

## Objective

- Create a behavior-based credit scoring model for DeFi wallets.
- Use transaction-level data from Aave V2 (deposit, borrow, repay, liquidation, etc.)
- Output a credit score between **0–1000** per wallet.

---

## Project Structure

```
aave-credit-score/
├── data/
│   └── user_transactions.json
├── src/
│   └── score_generator.py
├── output/
│   ├── wallet_scores.csv
│   └── score_distribution.png
├── README.md
└── analysis.md
```

---

## Features Engineered

| Feature | Description |
|--------|-------------|
| `total_deposits` | Total amount deposited |
| `total_borrows` | Total amount borrowed |
| `total_repays` | Total amount repaid |
| `borrow_repay_ratio` | Repayments relative to borrows |
| `num_deposits` | Number of deposit actions |
| `num_liquidations` | Number of liquidation events |
| `unique_tokens_used` | Diversity of tokens used |
| `avg_time_between_actions` | Frequency of wallet activity |
| `redeem_to_deposit_ratio` | Risky churn behavior indicator |

---

## Scoring Logic

Final Score = Weighted sum of normalized features:

- **25%** – Repayment behavior (repay/borrow)
- **15%** – Total deposits
- **15%** – Number of deposits
- **15%** – Token diversity
- **10%** – Inverse liquidation count
- **10%** – Inverse redemption ratio
- **10%** – Frequency of wallet usage

---

## How to Run

```bash
# Step 1: Place JSON file in 'data/user_transactions.json'
# Step 2: Run the script
python src/score_generator.py
```

---

## Output

- `output/wallet_scores.csv` – Wallet address + credit score
- `output/score_distribution.png` – Histogram of credit scores

---

## Deliverables

- `README.md` – Project overview & methodology
- `analysis.md` – Score-based wallet behavior analysis
