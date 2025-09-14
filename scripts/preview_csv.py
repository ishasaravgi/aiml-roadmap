import pandas as pd
import sys

# Accept file path from command line OR default to iris.csv
file_path = sys.argv[1] if len(sys.argv) > 1 else "data/iris.csv"

# Load CSV
df = pd.read_csv(file_path)

print("Shape:", df.shape)  # rows, cols
print("\nColumns:", df.columns.tolist())
print("\nData types:\n", df.dtypes)

# Basic stats for numeric columns
print("\nSummary statistics:\n", df.describe())

