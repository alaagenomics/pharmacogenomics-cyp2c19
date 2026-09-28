import pandas as pd

# Input files
variant_file = "data/processed/cyp2c19_variant_metadata.tsv"
population_file = "data/processed/cyp2c19_population_frequencies.tsv"
cpic_file = "data/processed/cpic_cyp2c19_clopidogrel.tsv"

# Read project datasets
variant = pd.read_csv(
    variant_file,
    sep="\t"
)

population = pd.read_csv(
    population_file,
    sep="\t"
)

cpic = pd.read_csv(
    cpic_file,
    sep="\t"
)

# Extract CYP2C19*2 metadata
variant_info = variant.iloc[0]

print("=== CYP2C19*2 Integrated Pharmacogenomics Analysis ===")

print("\n=== Variant Information ===")
print(f"Drug: {variant_info['drug']}")
print(f"Gene: {variant_info['gene']}")
print(f"Star allele: {variant_info['star_allele']}")
print(f"rsID: {variant_info['rsid']}")
print(f"Molecular change: {variant_info['molecular_change']}")
print(f"Function: {variant_info['function']}")
print(f"Evidence source: {variant_info['evidence_source']}")
print(f"Evidence level: {variant_info['evidence_level']}")

# Population frequency summary
highest = population.loc[
    population["allele_frequency"].idxmax()
]

lowest = population.loc[
    population["allele_frequency"].idxmin()
]

mean_frequency = population["allele_frequency"].mean()

print("\n=== Population Frequency Summary ===")
print(f"Number of ancestry groups: {len(population)}")
print(f"Mean allele frequency: {mean_frequency:.4f}")
print(
    f"Highest allele frequency: "
    f"{highest['ancestry_group']} "
    f"({highest['allele_frequency']:.4f})"
)
print(
    f"Lowest allele frequency: "
    f"{lowest['ancestry_group']} "
    f"({lowest['allele_frequency']:.4f})"
)

# CPIC phenotype summary
print("\n=== CPIC Genotype-to-Phenotype Summary ===")

for _, row in cpic.iterrows():
    print(
        f"{row['genotype_example']} -> "
        f"{row['phenotype']}"
    )

# Create integrated summary table
summary = pd.DataFrame({
    "drug": [variant_info["drug"]],
    "gene": [variant_info["gene"]],
    "star_allele": [variant_info["star_allele"]],
    "rsid": [variant_info["rsid"]],
    "molecular_change": [variant_info["molecular_change"]],
    "function": [variant_info["function"]],
    "highest_frequency_group": [highest["ancestry_group"]],
    "highest_frequency": [highest["allele_frequency"]],
    "lowest_frequency_group": [lowest["ancestry_group"]],
    "lowest_frequency": [lowest["allele_frequency"]],
    "mean_frequency": [mean_frequency]
})

# Save integrated summary
output_file = "data/processed/cyp2c19_integrated_summary.tsv"

summary.to_csv(
    output_file,
    sep="\t",
    index=False
)

print(
    f"\nIntegrated summary saved to: {output_file}"
)
