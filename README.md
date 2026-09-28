# CYP2C19 Pharmacogenomics Analysis

A reproducible Python-based pharmacogenomics project analyzing the CYP2C19*2 variant and its relationship to clopidogrel response.

## Project Overview

This project examines the pharmacogenomic relationship between the antiplatelet drug clopidogrel and the CYP2C19 gene, focusing on the CYP2C19*2 star allele (rs4244285).

The analysis integrates:

- Variant annotation and pharmacogenomic evidence from PharmGKB/ClinPGx
- Population allele-frequency data from gnomAD v4.1.1
- CYP2C19*2 genotype-to-phenotype relationships
- Clinical recommendations from CPIC
- Python-based data processing and visualization

The goal is to demonstrate a reproducible computational pharmacogenomics workflow using publicly available genomic and clinical resources.

## Drug-Gene Pair

| Field | Value |
|---|---|
| Drug | Clopidogrel |
| Gene | CYP2C19 |
| Star allele | *2 |
| Variant | rs4244285 |
| Molecular change | c.681G>A |
| Functional classification | No function |
| Evidence source | PharmGKB/ClinPGx |
| Evidence level | 1A |

CYP2C19*2 is a no-function allele associated with abnormal CYP2C19 splicing and reduced functional enzyme activity.

## Data Sources

### PharmGKB / ClinPGx

Pharmacogenomic evidence was used to identify the CYP2C19-clopidogrel relationship, the CYP2C19*2 allele, and its functional classification.

### gnomAD

Population-frequency data were obtained from gnomAD v4.1.1 using GRCh38 and combined Exomes + Genomes data.

The analyzed variant was:

```text
10-94781859-G-A
