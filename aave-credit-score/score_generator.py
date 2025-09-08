import json
import pandas as pd
import numpy as np
from tqdm import tqdm
import os

def load_transactions(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return pd.DataFrame(data)

def engineer_features(df):
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    grouped = df.groupby('wallet')

    features = pd.DataFrame()
    features['total_deposits'] = grouped.apply(lambda x: x[x.action == 'deposit']['amount'].sum())
    features['total_borrows'] = grouped.apply(lambda x: x[x.action == 'borrow']['amount'].sum())
    features['total_repays'] = grouped.apply(lambda x: x[x.action == 'repay']['amount'].sum())
    features['borrow_repay_ratio'] = features['total_repays'] / (features['total_borrows'] + 1e-5)
    features['num_deposits'] = grouped.apply(lambda x: (x.action == 'deposit').sum())
    features['num_liquidations'] = grouped.apply(lambda x: (x.action == 'liquidationcall').sum())
    features['unique_tokens_used'] = grouped['token'].nunique()
    features['num_actions'] = grouped.size()

    avg_time = grouped['timestamp'].apply(lambda x: x.sort_values().diff().dt.total_seconds().mean())
    features['avg_time_between_actions'] = avg_time.fillna(0)

    features['redeem_to_deposit_ratio'] = grouped.apply(lambda x: x[x.action == 'redeemunderlying']['amount'].sum()) / (features['total_deposits'] + 1e-5)
    features = features.fillna(0)

    return features

def calculate_score(features):
    normed = (features - features.min()) / (features.max() - features.min() + 1e-6)
    score = (
        0.25 * normed['borrow_repay_ratio'] +
        0.15 * normed['total_deposits'] +
        0.15 * normed['num_deposits'] +
        0.10 * (1 - normed['redeem_to_deposit_ratio']) +
        0.10 * (1 - normed['num_liquidations']) +
        0.10 * (1 - normed['avg_time_between_actions']) +
        0.15 * normed['unique_tokens_used']
    )
    features['credit_score'] = (score * 1000).clip(0, 1000).astype(int)
    return features[['credit_score']]

def save_score_distribution(scores, out_path):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.hist(scores['credit_score'], bins=10, edgecolor='black')
    plt.title('Wallet Credit Score Distribution')
    plt.xlabel('Score Range')
    plt.ylabel('Number of Wallets')
    plt.savefig(out_path)

def main():
    os.makedirs('output', exist_ok=True)
    df = load_transactions('data/user_transactions.json')
    features = engineer_features(df)
    scores = calculate_score(features)
    scores.reset_index().to_csv('output/wallet_scores.csv', index=False)
    save_score_distribution(scores, 'output/score_distribution.png')
    print("✅ Credit scores and graph saved in output/")

if __name__ == "__main__":
    main()