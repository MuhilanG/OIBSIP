# EDA on Retail Sales Data

**Oasis Infobyte Internship — Data Analytics · Level 1 · Task 1**

A thorough Exploratory Data Analysis of a retail sales dataset to uncover sales patterns, customer behaviour trends, and actionable business insights.

---

## Dataset

- **Source:** [Retail Sales Dataset — Kaggle](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)
- **License:** CC0: Public Domain
- **Contents:** 1,000 transactions spanning **Jan 2023 – Jan 2024**

| Column | Description |
|---|---|
| Transaction ID | Unique transaction identifier |
| Date | Transaction date |
| Customer ID | Customer identifier |
| Gender | Customer gender (Male / Female) |
| Age | Customer age (18–64) |
| Product Category | Beauty / Clothing / Electronics |
| Quantity | Units purchased per transaction (1–4) |
| Price per Unit | Price of a single unit ($25–$500) |
| Total Amount | Total monetary value of the transaction |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Language |
| pandas / NumPy | Data manipulation & statistics |
| matplotlib / seaborn | Visualisations |
| Jupyter Notebook | Deliverable format |

---

## Project Structure

```
DataAnalytics-L1-EDARetailSales/
├── EDA_Retail_Sales.ipynb   # Main notebook (executed, with outputs)
├── retail_sales_dataset.csv # Input data
├── README.md                # This file
└── screenshots/             # Chart outputs (also embedded in the notebook)
```

---

## How to Run

```bash
# 1. Install dependencies
pip install pandas numpy matplotlib seaborn jupyterlab

# 2. Launch JupyterLab from this folder
jupyter lab

# 3. Open EDA_Retail_Sales.ipynb and run all cells (or re-execute from the top)
```

---

## Feature Checklist Coverage

| Requirement | Covered |
|---|---|
| Load dataset + inspection (shape, dtypes, nulls) | ✅ Section 1 |
| Descriptive stats (mean, median, mode, std) | ✅ Section 2 |
| Monthly & quarterly sales trend line charts | ✅ Section 4 |
| Age-group distribution + gender breakdown | ✅ Section 5 |
| Top best-selling products / categories + revenue by category | ✅ Section 6 |
| Correlation heatmap | ✅ Section 7 |
| Additional non-obvious insight | ✅ Section 8 (weekday vs. weekend) |
| Markdown observations after each chart | ✅ Throughout |
| ≥3 actionable business recommendations | ✅ Section 9 (4 recommendations) |

---

## Key Findings

1. **Strong seasonality, flat overall** — revenue swings from a **September trough ($23.6k)** to a **May peak ($53.2k)**; Q4 2023 is the strongest quarter ($126.2k).
2. **Unit price, not volume, drives revenue** — `Price per Unit` correlates **+0.85** with `Total Amount`; Electronics earns the most revenue ($156.9k) while Clothing only moves the most units (894).
3. **Younger customers spend more per order** — average order value falls from **≈ $500 (18–25)** to **≈ $412 (56+)**. 46–55 is the busiest band; gender split is nearly even (51/49).
4. **Weekend effect** — **Saturday alone contributes 17.3%** of weekly revenue (vs. 11.8% for the slowest day, Thursday); weekends bring 30.1% of weekly revenue.

### Recommendations (summary)
- Push promotions in the weak months (Sep, Mar) and staff/stock for May, Oct, Dec peaks.
- Upsell premium/bundled electronics to raise the median order value ($135).
- Focus ads and staffing on Saturdays; use Thursdays for low-cost maintenance.
- Curate premium ranges for the high-value 18–25 segment while serving the high-volume 46–55 band.

---

## Screenshots

Charts are rendered inline in the notebook and saved to `screenshots/`:

1. `01_monthly_sales_trend.png` — monthly revenue
2. `02_quarterly_sales_trend.png` — quarterly revenue
3. `03_gender_breakdown.png` — bar + pie
4. `04_age_group_distribution.png` — age bands
5. `05_avg_spend_age_gender.png` — AOV by age × gender
6. `06_revenue_by_category.png` — category revenue
7. `07_best_selling_categories.png` — units by category
8. `08_quantity_by_category.png` — quantity boxplots
9. `09_correlation_heatmap.png` — feature correlations
10. `10_weekday_sales_pattern.png` — day-of-week insight

---

*Prepared for the Oasis Infobyte Data Analytics Internship — Level 1 · Task 1.*