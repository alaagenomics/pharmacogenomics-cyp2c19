import pandas as pd
import matplotlib.pyplot as plt

# Input file
input_file = "data/processed/cpic_cyp2c19_clopidogrel.tsv"

# Read CPIC data
df = pd.read_csv(
    input_file,
    sep="\t"
)

# Create ordered phenotype labels
phenotype_order = [
    "Normal Metabolizer",
    "Intermediate Metabolizer",
    "Poor Metabolizer"
]

df["phenotype"] = pd.Categorical(
    df["phenotype"],
    categories=phenotype_order,
    ordered=True
)

df = df.sort_values("phenotype")

# Create numeric positions for the phenotypes
x_positions = range(len(df))

plt.figure(figsize=(9, 6))

plt.bar(
    x_positions,
    [1] * len(df)
)

plt.xticks(
    x_positions,
    df["genotype_example"]
)

plt.xlabel("Example CYP2C19 Diplotype")
plt.ylabel("Metabolizer Phenotype")
plt.title("CYP2C19 Genotype-to-Phenotype Relationship")

# Add phenotype labels above each bar
for i, phenotype in enumerate(df["phenotype"]):
    plt.text(
        i,
        1.02,
        phenotype,
        ha="center",
        va="bottom"
    )

plt.ylim(0, 1.25)
plt.yticks([])

plt.tight_layout()

# Save figure
output_file = "results/figures/cpic_genotype_phenotype.png"

plt.savefig(
    output_file,
    dpi=300
)

print(f"Figure saved to: {output_file}")

plt.show()
