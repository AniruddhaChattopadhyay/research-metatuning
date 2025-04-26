import pandas as pd
from tqdm import tqdm
import time

# Create a sample dataframe
df = pd.DataFrame({
    'A': range(100),
    'B': range(100, 200),
    'C': range(200, 300)
})

print("Method 1: Using iterrows()")
for _, row in tqdm(df.iterrows(), total=len(df)):
    # Simulate some processing
    time.sleep(0.01)
    # Access columns using row['column_name']
    # print(row['A'], row['B'])

print("\nMethod 2: Using itertuples()")
for row in tqdm(df.itertuples(), total=len(df)):
    # Simulate some processing
    time.sleep(0.01)
    # Access columns using row.column_name
    # print(row.A, row.B)

print("\nMethod 3: Using progress_apply()")
tqdm.pandas()  # Enable tqdm for pandas

def process_row(row):
    # Simulate some processing
    time.sleep(0.01)
    return row['A'] + row['B']

# Apply the function to each row
df['sum'] = df.progress_apply(process_row, axis=1)

# Note: For large DataFrames, itertuples() is generally the fastest method
# and uses less memory than iterrows() 