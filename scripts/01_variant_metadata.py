import pandas as pd

variant = {
    "drug": "clopidogrel",
    "gene": "CYP2C19",
    "star_allele": "*2",
    "rsid": "rs4244285",
    "molecular_change": "c.681G>A",
    "function": "No function"
}

df = pd.DataFrame([variant])

print(df.to_string(index=False))

output_file = "../data/processed/cyp2c19_variant_metadata.tsv"

df.to_csv(
    output_file,
    sep="\t",
    index=False
)

print(f"\nMetadata saved to: {output_file}")
