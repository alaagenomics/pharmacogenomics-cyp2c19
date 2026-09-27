import pandas as pd
import matplotlib.pyplot as plt

# Input file
input_file = "data/processed/cyp2c19_population_frequencies.tsv"

# Read processed population data
df = pd.read_csv(
    input_file,
    sep="\t"
)

# Convert frequency to percentage
df["frequency_percent"] = df["allele_frequency"] * 100

# Sort from lowest to highest frequency
df = df.sort_values("frequency_percent")

# Create plot
plt.figure(figsize=(10, 6))

plt.bar(
    df["ancestry_group"],
    df["frequency_percent"]
)

plt.xlabel("Ancestry Group")
plt.ylabel("CYP2C19*2 Allele Frequency (%)")
plt.title("CYP2C19*2 Allele Frequency by Ancestry Group")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save figure
output_file = "results/figures/cyp2c19_star2_population_frequency.png"

plt.savefig(
    output_file,
    dpi=300
)

print(f"Figure saved to: {output_file}")

plt.show()
