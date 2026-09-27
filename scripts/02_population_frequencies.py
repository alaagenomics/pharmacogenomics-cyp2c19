import pandas as pd

# Input file
input_file = "data/raw/gnomad_cyp2c19_star2.tsv"

# Read gnomAD population data
df = pd.read_csv(
    input_file,
    sep="\t"
)

print("=== gnomAD CYP2C19*2 Population Data ===")
print(df.to_string(index=False))

# Check data types
print("\n=== Data Types ===")
print(df.dtypes)

# Basic summary
print("\n=== Frequency Summary ===")
print(df["allele_frequency"].describe())

# Highest frequency
highest = df.loc[df["allele_frequency"].idxmax()]

print("\n=== Highest Allele Frequency ===")
print(highest.to_string())

# Lowest frequency
lowest = df.loc[df["allele_frequency"].idxmin()]

print("\n=== Lowest Allele Frequency ===")
print(lowest.to_string())

# Save processed data
output_file = "data/processed/cyp2c19_population_frequencies.tsv"

df.to_csv(
    output_file,
    sep="\t",
    index=False
)

print(f"\nProcessed data saved to: {output_file}")
