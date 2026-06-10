"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-XXXX
Name: Your Name Here

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV
==============================================================
"""

import json
import pandas as pd
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = "raw_data.json"
OUTPUT_FILE = "processed_data.csv"


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.

    Returns:
        list: Danh sach cac records
    """
    print(f"Extracting data from {file_path}...")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f"Extract complete. Records extracted: {len(data)}")
        return data

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []

    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file - {file_path}")
        return []


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.

    Quy tac:
       - price phai > 0
       - category khong duoc rong

    Returns:
        list: Danh sach records hop le
    """
    valid_records = []
    error_count = 0

    for record in data:
        price = record.get("price", 0)
        category = record.get("category")

        is_valid_price = isinstance(price, (int, float)) and price > 0
        is_valid_category = category is not None and str(category).strip() != ""

        if is_valid_price and is_valid_category:
            valid_records.append(record)
        else:
            error_count += 1

    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    return valid_records


def transform(data):
    """
    Task 3: Transform du lieu.

    Yeu cau:
       - discounted_price = price * 0.9
       - category thanh Title Case
       - them processed_at
    """
    df = pd.DataFrame(data)

    if df.empty:
        print("Transform skipped: No valid data.")
        return df

    df["discounted_price"] = df["price"] * 0.9
    df["category"] = df["category"].str.title()
    df["processed_at"] = datetime.datetime.now().isoformat()

    print(f"Transform complete. Processed records: {len(df)}")
    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None:
            load(final_df, OUTPUT_FILE)
            print(f"\nPipeline completed! {len(final_df)} records saved.")
        else:
            print("\nTransform returned None. Check your transform() function.")
    else:
        print("\nPipeline aborted: No data extracted.")