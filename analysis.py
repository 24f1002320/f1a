# analysis.py
# Email for verification: 24f1002320@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# ---------- Data setup ----------

data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "CAC": [226.71, 226.31, 231.69, 234.56],
}

industry_target = 150

df = pd.DataFrame(data)

# Compute average CAC to verify requirement
average_cac = df["CAC"].mean()
print(f"Average CAC (2024): {average_cac:.2f}")  # should be 229.82

# ---------- Visualization ----------

plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots(figsize=(8, 5))

# Line + scatter for CAC trend
ax.plot(df["Quarter"], df["CAC"], marker="o", label="CAC (2024)", linewidth=2)
ax.scatter(df["Quarter"], df["CAC"], s=80)

# Horizontal benchmark line
ax.axhline(y=industry_target, color="red", linestyle="--", label="Industry Target (150)")

# Annotate last point and average
ax.annotate(
    f"Q4: {df['CAC'].iloc[-1]:.2f}",
    xy=(df["Quarter"].iloc[-1], df["CAC"].iloc[-1]),
    xytext=(0, 10),
    textcoords="offset points",
    ha="center",
    fontsize=9,
)

ax.annotate(
    f"Avg CAC: {average_cac:.2f}",
    xy=(1.5, average_cac),
    xytext=(0, 10),
    textcoords="offset points",
    fontsize=9,
    color="black",
)

# Labels and title
ax.set_title("Customer Acquisition Cost (CAC) – 2024 Quarterly Trend", fontsize=14, weight="bold")
ax.set_xlabel("Quarter")
ax.set_ylabel("CAC ($)")

# Y-axis: start near 140 to show gap to target clearly
ax.set_ylim(140, max(df["CAC"]) + 10)

ax.legend()

fig.tight_layout()

# Save visualization
plt.savefig("cac_trend.png", dpi=150)
plt.close()

# ---------- Simple text summary in console ----------

gap_to_target = average_cac - industry_target
percent_above_target = (gap_to_target / industry_target) * 100

print(f"Industry target CAC: {industry_target}")
print(f"Average CAC gap: {gap_to_target:.2f} ({percent_above_target:.1f}% above target)")
print("Key issue: Rising CAC vs stable, much lower industry benchmark.")
