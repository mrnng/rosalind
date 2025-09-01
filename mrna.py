# Inferring mRNA from Protein
# Problem link: https://rosalind.info/problems/mrna/

import utils
import pyperclip
from collections import Counter

filepath = utils.get_filepath("mrna")

amino_acid_counts = Counter(utils.CODON_TABLE.values())

def count_mrna_sequences(protein):
    mod = 1_000_000
    result = 1
    for a in protein:
        result = (result * amino_acid_counts[a]) % mod
    # there are 3 possible stop codons
    return (result * 3) % mod

with open(filepath, "r") as f:
    protein = f.read().strip()

result = count_mrna_sequences(protein)

pyperclip.copy(result)
print(result)