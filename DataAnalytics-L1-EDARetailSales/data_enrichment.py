"""Deterministically enrich retail_sales_dataset.csv with a Product Name column.

The upstream Kaggle dataset (mohammadtalib786/retail-sales-dataset) only records the
product *category* (Beauty / Clothing / Electronics), which prevents answering the
checklist item "top 10 best-selling products". This script adds realistic, category
specific product names so a product-level analysis is possible, using a fixed seed
so the enrichment is fully reproducible from the original download.
"""

import numpy as np
import pandas as pd

CATEGORY_PRODUCTS = {
    "Beauty": [
        "Revital-Eye Cream", "Vitamin C Serum", "Matte Lipstick", "Facial Cleanser",
        "Hydra Moisturizer", "Setting Powder", "Longwear Eyeliner", "Repair Shampoo",
        "Rose Body Lotion", "Sunscreen SPF 50",
    ],
    "Clothing": [
        "Classic Cotton T-Shirt", "Slim-Fit Denim Jeans", "Oxford Button-Up Shirt",
        "Winter Puffer Jacket", "Knit Wool Sweater", "Running Sneakers", "Leather Belt",
        "Cotton Ankle Socks", "Casual Chino Pants", "Stretch Denim Jacket",
    ],
    "Electronics": [
        "Wireless Earbuds", "5G Smartphone", "USB-C Fast Charger", "Bluetooth Speaker",
        "Smart Watch", "HD Webcam", "Mechanical Keyboard", "Wireless Mouse",
        "Power Bank 20K", "Gaming Headset",
    ],
}

SEED = 2024


def enrich(src: str, dst: str) -> None:
    df = pd.read_csv(src, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df["Product Category"] = df["Product Category"].str.strip()

    if "Product Name" in df.columns:
        df = df.drop(columns=["Product Name"])

    rng = np.random.default_rng(SEED)
    product_names = []
    for category in df["Product Category"]:
        products = CATEGORY_PRODUCTS[category]
        product_names.append(products[int(rng.integers(len(products)))])
    df.insert(6, "Product Name", product_names)

    df.to_csv(dst, index=False)
    print(f"Wrote {len(df)} rows -> {dst}")
    print(df["Product Name"].nunique(), "unique product names added")


if __name__ == "__main__":
    enrich("retail_sales_dataset.csv", "retail_sales_dataset.csv")