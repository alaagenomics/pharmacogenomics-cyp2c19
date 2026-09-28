import pandas as pd

# Input file
input_file = "data/raw/cpic_cyp2c19_clopidogrel.tsv"

# Read CPIC data
df = pd.read_csv(
    input_file,
    sep="\t"
)

print("=== CPIC CYP2C19 / Clopidogrel Recommendations ===")
print(df.to_string(index=False))

print("\n=== Genotype to Phenotype Mapping ===")
print(
    df[
        [
            "genotype_example",
            "phenotype"
        ]
    ].to_string(index=False)
)

print("\n=== ACS/PCI Recommendations ===")
print(
    df[
        [
            "phenotype",
            "acs_pci_recommendation"
        ]
    ].to_string(index=False)
)

# Save processed data
output_file = "data/processed/cpic_cyp2c19_clopidogrel.tsv"

df.to_csv(
    output_file,
    sep="\t",
    index=False
)

print(f"\nProcessed CPIC data saved to: {output_file}")
