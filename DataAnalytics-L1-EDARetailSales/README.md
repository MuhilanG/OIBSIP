# EDA on Retail Sales Data

**Oasis Infobyte Internship — Data Analytics · Level 1 · Task 1**

A thorough Exploratory Data Analysis of a retail sales dataset to uncover sales patterns, customer behaviour trends, and actionable business insights.

---

## Dataset

- **Source:** [Retail Sales Dataset — Kaggle](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)
- **License:** CC0: Public Domain
- **Contents:** 1,000 transactions dated **1 Jan 2023 – 1 Jan 2024**
  (⚠️ the final day contributes only **2 rows**, so Jan-2024 is a *partial* month — see [Known limitations](#known-limitations))

| Column | Description |
|---|---|
| Transaction ID | Unique transaction identifier |
| Date | Transaction date |
| Customer ID | Customer identifier |
| Gender | Customer gender (Male / Female) |
| Age | Customer age (18–64) |
| Product Category | Beauty / Clothing / Electronics |
| Product Name | Synthetic product-level SKU — see [Data provenance](#data-provenance) |
| Quantity | Units purchased per transaction (1–4) |
| Price per Unit | Price of a single unit — only 5 distinct values exist ($25–$500) |
| Total Amount | Total monetary value = `Quantity × Price per Unit` on every row |

> ### Data provenance
>
> ⚠️ **This is a synthetic dataset.** The source file is a **teaching/synthetic dataset**, not a record
> of real retail activity. This is verifiable from the data itself, not assumed:
>
> | Signal | Observation |
> |---|---|
> | Unit prices | only **5 distinct values** (25, 30, 50, 300, 500) |
> | Quantities | always between 1 and 4 |
> | `Total Amount` | exactly `Quantity × Price per Unit` on **every** row — a derived column, not an independent measure |
> | `Transaction ID` | sequential 1…1,000 |
> | Repeat behaviour | **1,000 rows = 1,000 distinct customers** — exactly one transaction per customer |
>
> **What this means for the results**
> 1. **The `Product Name` column does not exist in the source file.** The upstream dataset records only
>    the product *category*, which cannot answer the checklist item *"top 10 best-selling products"*.
>    It is therefore generated **deterministically** (fixed seed `2024`) by `data_enrichment.py`, which
>    assigns one of 30 realistic, category-specific SKU names per row. Run that script to reproduce the
>    column byte-for-byte from the original download. Product-level rankings consequently describe the
>    **enrichment method**, not real products — the notebook states this at the point of use and prints
>    it on the product chart itself.
> 2. The figures below are **properties of this sample**, not evidence about a real business. They are
>    reported in full because they exercise every analytical step the task requires. What the project
>    demonstrates is the **method** — inspection, cleaning, descriptive statistics, time series,
>    segmentation, correlation — which transfers to a production dataset unchanged.

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
├── retail_sales_dataset.csv # Input data (enriched with Product Name)
├── data_enrichment.py       # Reproducible product-name enrichment script
├── README.md                # This file
└── screenshots/             # Chart outputs (also embedded in the notebook)
```

---

## How to Run

```bash
# 1. Install dependencies
pip install pandas numpy matplotlib seaborn jupyterlab

# 2. (Optional) regenerate the Product Name column from the original download.
#    Deterministic — fixed seed 2024 — so it always reproduces the same SKUs.
python data_enrichment.py

# 3. Launch JupyterLab from this folder
jupyter lab

# 4. Open EDA_Retail_Sales.ipynb and run all cells (or re-execute from the top)
```

> Verified: the notebook re-executes top-to-bottom with **zero errors** and regenerates all 10
> screenshots in `screenshots/`.

---

## Feature Checklist Coverage

| Requirement | Covered |
|---|---|
| Load dataset + inspection (shape, dtypes, nulls) | ✅ Section 1 |
| Descriptive stats (mean, median, mode, std) | ✅ Section 2 |
| Monthly & quarterly sales trend line charts | ✅ Section 4 |
| Age-group distribution + gender breakdown | ✅ Section 5 |
| Top best-selling products + revenue by category | ✅ Section 6 (top 10 by revenue & units) |
| Correlation heatmap | ✅ Section 7 |
| Additional non-obvious insight | ✅ Section 8 (weekday vs. weekend) |
| Markdown observations after each chart | ✅ Throughout |
| ≥3 actionable business recommendations | ✅ Section 9 (4 recommendations) |

---

## Key Findings

> Read against the [provenance note](#data-provenance) above: these characterise **this synthetic
> sample**, and are presented to demonstrate the analytical method.

1. **Strong seasonality, flat overall** — revenue swings from a **September trough ($23.6k)** to a **May peak ($53.2k)**; at quarterly level **Q4 2023 is the strongest ($126.2k)** and **Q3 2023 the weakest ($96.0k)** — a classic end-of-year boost. *(Jan-2024 shows only $1.5k because the dataset ends on 1 Jan 2024 — it is a partial month, not a collapse in sales.)*
2. **Unit price, not volume, drives revenue** — `Price per Unit` correlates **+0.85** with `Total Amount`; Electronics earns the most revenue ($156.9k) while Clothing only moves the most units (894).
3. **Younger customers spend more per order** — average order value falls from **≈ $500 (18–25)** to **≈ $412 (56+)**. 46–55 is the busiest band; gender split is nearly even (51/49).
4. **Weekend effect** — **Saturday alone contributes 17.3%** of weekly revenue (vs. 11.8% for the slowest day, Thursday); weekends bring 30.1% of weekly revenue.
5. **Product-level best sellers** — **Running Sneakers** tops *both* revenue (**$26.1k**) and units (131); the top-10 products deliver **43.6%** of total revenue, with Electronics SKUs (Mechanical Keyboard, Wireless Earbuds, USB-C Fast Charger) dominating the value list. *(Product names are synthetic — see the provenance note.)*

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
7. `07_top10_products_revenue.png` — top 10 products by revenue (carries the synthetic-SKU caveat in its title)
8. `08_quantity_by_category.png` — quantity boxplots
9. `09_correlation_heatmap.png` — feature correlations
10. `10_weekday_sales_pattern.png` — day-of-week insight

---

## Known limitations

Stated explicitly so the analysis is not over-read:

| # | Limitation | Effect on the analysis |
|---|---|---|
| 1 | The source dataset is **synthetic** (see provenance note) | All figures describe this sample, not a real business. The value delivered is the method. |
| 2 | **`Product Name` is generated**, not observed | The "top 10 best-selling products" ranking reflects the fixed-seed assignment in `data_enrichment.py`. Category-level findings (Sections 5–6) are unaffected, because `Product Category` **is** in the source file. |
| 3 | **1,000 rows = 1,000 distinct customers** — one transaction each | Repeat purchase, retention, customer lifetime value and RFM segmentation are **not** computable. Frequency-based analysis would need a transactional dataset with repeat customers. |
| 4 | **`Total Amount` = `Quantity × Price per Unit`** on every row | It is a derived column, so its +0.85 correlation with unit price is partly arithmetic, not an empirical discovery. It is still a useful proxy for basket value. |
| 5 | **Jan-2024 is a partial month** (2 rows, 1 Jan only) | Its $1.5k is not a demand collapse. Month-over-month comparisons should exclude it; the analysis compares **September** as the trough among complete months. |
| 6 | Only **5 distinct unit prices** and quantities of 1–4 | Price is heavily quantised, which flattens distribution shapes (e.g. the `Price per Unit` median of $50 vs. mean of $180 is driven by a few high-price rows, not a smooth spread). |
| 7 | **Age and gender are attributes of a single one-off transaction** | No tenure or lifecycle information exists, so demographic findings describe *purchase occasion*, not customer cohorts. |

**What I would do with a production dataset:** validate `Total Amount` against invoices, confirm repeat customers exist for retention analysis, replace the generated product column with real SKUs, and re-test the seasonality finding across multiple years before acting on it commercially.

---

*Prepared for the Oasis Infobyte Data Analytics Internship — Level 1 · Task 1.*