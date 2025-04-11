import pandas as pd
import matplotlib.pyplot as plt
import argparse
from scipy.stats import pearsonr
import numpy as np

def plot_tmscore_vs_plddt(result_csv, summary_csv, output_path="scatter_tmscore_plddt.png"):
    # Load data
    df_results = pd.read_csv(result_csv).iloc[1:]  # Skip reference PDB
    df_summary = pd.read_csv(summary_csv)

    # Align length
    min_len = min(len(df_results), len(df_summary))
    df_results = df_results.iloc[:min_len]
    df_summary = df_summary.iloc[:min_len]

    # Extract values
    tmscore = df_summary["tmscore_to_label_by_label"].astype(float)
    plddt = df_results["plddt"].astype(float) / 100  # Normalize pLDDT

    # Compute Pearson correlation
    corr, _ = pearsonr(tmscore, plddt)
    print(f"📈 Pearson correlation (TMscore vs. pLDDT): {corr:.4f}")

    # Fit linear regression for trend line
    slope, intercept = np.polyfit(tmscore, plddt, deg=1)
    fit_line = slope * tmscore + intercept

    # Scatter plot + linear fit
    plt.figure(figsize=(6, 6))
    plt.scatter(tmscore, plddt, alpha=0.7, label="Data points")
    plt.plot(tmscore, fit_line, color="red", label=f"Linear fit (r = {corr:.2f})")
    plt.xlabel("TMscore (label)")
    plt.ylabel("pLDDT / 100 (AF2Rank)")
    plt.title("TMscore vs. pLDDT")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"✅ Scatter plot saved to: {output_path}")
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot TMscore vs pLDDT with linear fit.")
    parser.add_argument("result_csv", help="Path to results.csv")
    parser.add_argument("summary_csv", help="Path to summary.csv")
    parser.add_argument("--output", default="scatter_tmscore_plddt.png", help="Output plot filename")

    args = parser.parse_args()
    plot_tmscore_vs_plddt(args.result_csv, args.summary_csv, args.output)
