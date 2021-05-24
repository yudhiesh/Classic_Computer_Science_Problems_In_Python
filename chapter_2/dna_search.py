from enum import IntEnum
from typing import Tuple, List
from pprint import pprint

Nucleotide: IntEnum = IntEnum("Nucleotide", ("A", "C", "G", "T"))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type: ignore
Gene = List[Codon]
gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])  # type: ignore
        gene.append(codon)
    return gene


my_gene: Gene = string_to_gene(s=gene_str)


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


sample: Codon = (Nucleotide.A, Nucleotide.A, Nucleotide.A)  # type: ignore
assert not linear_contains(gene=my_gene, key_codon=sample)
sample2: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)  # type: ignore
assert linear_contains(gene=my_gene, key_codon=sample2)


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        middle: int = (high + low) // 2
        if gene[middle] < key_codon:
            low = middle + 1
        elif gene[middle] > key_codon:
            high = middle - 1
        else:
            return True
    return False


my_sorted_gene: Gene = sorted(my_gene)
sample: Codon = (Nucleotide.A, Nucleotide.A, Nucleotide.A)  # type: ignore
assert not binary_contains(gene=my_sorted_gene, key_codon=sample)
sample2: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)  # type: ignore
assert binary_contains(gene=my_sorted_gene, key_codon=sample2)
