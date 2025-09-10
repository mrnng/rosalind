# Inferring mRNA from Protein
# Problem link: https://rosalind.info/problems/mrna/

import pyperclip
from collections import Counter
from utils.io import get_filepath
from utils.bio import CODON_TABLE

filepath = get_filepath()

def solve(protein):
    amino_acid_counts = Counter(CODON_TABLE.values())
    mod = 1_000_000
    result = 1
    for a in protein:
        result = (result * amino_acid_counts[a]) % mod
    # There are 3 possible stop codons
    return (result * 3) % mod

if __name__ == "__main__":
    protein = filepath.read_text().strip()

    result = solve(protein)

    pyperclip.copy(result)
    print(result)