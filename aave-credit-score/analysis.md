# 📊 Score Analysis – Aave V2 Wallet Credit Scoring

---

## 🧭 Score Distribution

The wallet credit scores are distributed across the 0–1000 range. Below is the histogram of scores:

![Score Histogram](output/score_distribution.png)

---

## 🧮 Score Ranges

| Score Range | Wallet Count (Approx.) |
|-------------|------------------------|
| 0–100       | High-risk, frequent liquidations or zero repayments |
| 100–200     | Likely inactive or exploitative |
| 200–400     | Some activity, mixed reliability |
| 400–700     | Average, safe usage |
| 700–900     | Reliable users, well-behaved |
| 900–1000    | Highly trustworthy, repay consistently |

---

## 🧠 Behavior Observations

### 🔴 Low-Scoring Wallets (0–200)
- Rarely repay loans
- Often liquidated
- High redemption-to-deposit ratios
- Single-token usage (bot behavior)

### 🟢 High-Scoring Wallets (800–1000)
- Regular deposits and repayments
- High borrow-repay ratio
- Broad asset exposure
- Low liquidation frequency
- Consistent activity over time

---

## ✅ Conclusion

This model identifies DeFi wallet behavior patterns and can scale to other DeFi protocols. The score provides insights into user trustworthiness and can support lending platforms, risk assessments, or dApp integrations.