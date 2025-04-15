# utils.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

def load_latest_excel(folder="."):
    files = [f for f in os.listdir(folder) if f.startswith("shopee_voucher_unclaimed") and f.endswith(".xlsx")]
    if not files:
        return None
    latest_file = sorted(files)[-1]
    return pd.read_excel(os.path.join(folder, latest_file))

def generate_summary_plot(df, output_path="summary.png"):
    count_by_title = df["ชื่อคูปอง"].value_counts()
    plt.figure(figsize=(10, 6))
    count_by_title.plot(kind="bar")
    plt.title("สรุปประเภทคูปองที่เก็บได้")
    plt.ylabel("จำนวน")
    plt.tight_layout()
    plt.savefig(output_path)
    return output_path
