import pandas as pd
import numpy as np

# Load the dataframe
df = pd.read_csv("output_data/100_data_math500.csv")


# Function to analyze result pairs
def analyze_result_pair(df, base_col, compare_col):
    # Create a mask for non-blank values in both columns
    mask = df[base_col].notna() & df[compare_col].notna()

    # Get the filtered dataframe
    filtered_df = df[mask]

    print(f"\nAnalyzing {base_col} vs {compare_col}")
    print(f"Total rows after removing blanks: {len(filtered_df)}")

    # Get value counts for both columns
    print(f"\n{base_col} value counts:")
    print(filtered_df[base_col].value_counts())

    print(f"\n{compare_col} value counts:")
    print(filtered_df[compare_col].value_counts())

    # Calculate agreement
    agreement = (filtered_df[base_col] == filtered_df[compare_col]).mean() * 100
    print(f"\nAgreement between {base_col} and {compare_col}: {agreement:.2f}%")

    return filtered_df


# Analyze each pair
result_pairs = [
    ("result", "result_5"),
    ("result", "result_10"),
    ("result", "result_20"),
    ("result", "result_30"),
    ("result", "result_40"),
]

for base_col, compare_col in result_pairs:
    filtered_df = analyze_result_pair(df, base_col, compare_col)
    print("-" * 50)
