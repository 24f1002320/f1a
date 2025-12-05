# Financial Services Performance Analysis – CAC 2024

Email (for verification): **24f1002320@ds.study.iitm.ac.in**

## Business Context

As a senior data analyst in a financial services company, I was asked to investigate a rising **Customer Acquisition Cost (CAC)** trend. The executive team is concerned because:

- **Current average CAC (2024): 229.82**
- **Industry benchmark target CAC: 150**

The goal of this analysis is to provide a **data-driven story** and **actionable recommendations** to help the company move toward the industry target in the next fiscal year.

---

## Dataset

**Customer Acquisition Cost (CAC) – 2024 Quarterly Data**

| Quarter | CAC ($) |
|--------|---------|
| Q1     | 226.71  |
| Q2     | 226.31  |
| Q3     | 231.69  |
| Q4     | 234.56  |

- **Average CAC (2024): 229.82**
- **Industry Target: 150**

The data is processed and visualized in `analysis.py`.

---

## Analysis Approach

The analysis code is implemented in **`analysis.py`** using:

- `pandas` for data handling
- `matplotlib` for visualization

Steps:

1. Load quarterly CAC values into a `DataFrame`
2. Compute:
   - Average CAC across all quarters
   - Gap vs the industry benchmark (absolute and percentage)
3. Visualize:
   - Quarterly CAC trend line
   - Horizontal line at the **industry target (150)**
4. Highlight the widening gap in later quarters (Q3, Q4)

The resulting visualization is saved as **`cac_trend.png`**.

---

## Key Findings

1. **Average CAC is significantly above the benchmark**

   - Average CAC (2024): **229.82**
   - Industry benchmark: **150**
   - Absolute gap: **79.82 per customer**
   - This is **over 50% higher** than the target, indicating that the company is paying a substantial premium for each acquired customer.

2. **CAC shows a rising trend over the year**

   - Q1: 226.71  
   - Q2: 226.31  
   - Q3: 231.69  
   - Q4: 234.56  
   The pattern is **gradually increasing**, with Q4 being the **most expensive** quarter. This suggests that without intervention, CAC may continue to rise in the next fiscal year.

3. **Growing strategic risk**

   - Higher CAC compresses **profit margins**, especially if revenue per customer is not rising at the same pace.
   - Rising acquisition costs mean **less efficient marketing spend**, reducing the number of customers that can be acquired for a fixed budget.
   - Over time, this erodes **competitive positioning**, since competitors closer to the 150 benchmark can outspend more efficiently.

---

## Business Implications

- **Budget inefficiency**: For every new customer, the company is overspending by ~80 compared to the benchmark. At scale (e.g., thousands of customers), this becomes a multi-million-dollar issue.
- **Reduced ROI on marketing**: If CAC continues to rise while customer lifetime value (CLV) remains constant, return on marketing investment will decline.
- **Strategic constraints**: High CAC restricts the ability to test new markets or segments because each experiment becomes more expensive.

This makes CAC optimization a **priority initiative** for the next fiscal year.

---

## Recommendations

The core solution is to **optimize digital marketing channels**.

More specifically:

1. **Channel-Level CAC Analysis**
   - Break down CAC by **channel** (e.g., paid search, paid social, display, affiliates, email).
   - Identify **high-CAC channels** that are driving the average up.
   - Reallocate budget from **underperforming** channels to **high-ROI** channels.

2. **Targeting and Audience Optimization**
   - Refine audience segments based on:
     - Historical performance
     - Conversion propensity
   - Use **lookalike audiences** and **negative audiences** to focus spend on high-intent users.

3. **Creative and Landing Page Optimization**
   - Run structured **A/B tests** on:
     - Ad creatives (messaging, visuals, CTAs)
     - Landing pages (headline, form length, page load speed)
   - Improve **conversion rate (CVR)** to reduce CAC without necessarily cutting spend.

4. **Bid Strategy and Budget Management**
   - Move from manual bidding to **smart bidding / algorithmic bidding** where appropriate.
   - Implement **bid caps** for low-performing segments and **raise caps** on high-performing ones.
   - Smooth budgets across the quarter to avoid last-minute spikes in spend that can drive up CAC.

5. **Measurement and Attribution**
   - Ensure accurate tracking across all digital channels (UTM parameters, pixels, server-side tracking where possible).
   - Use multi-touch attribution or data-driven attribution to understand **which channels truly contribute** to conversions.

---

## Summary

- The **current CAC of 229.82** is well above the **industry target of 150**, creating immediate profitability and competitiveness concerns.
- The **quarterly trend is upward**, with Q4 CAC the highest, suggesting that the problem is **intensifying over time**.
- A focused strategy to **optimize digital marketing channels** — through channel mix, targeting, creative, bidding, and attribution improvements — is necessary to move toward the target CAC of 150 in the next fiscal year.

All analysis and visualization used for this data story are contained in:

- `analysis.py` – code to process data and generate the visualization  
- `cac_trend.png` – chart showing CAC trend vs benchmark
