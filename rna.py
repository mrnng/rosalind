# Transcribing DNA into RNA
# Problem link: https://rosalind.info/problems/rna/

import utils
import pyperclip

filepath = utils.get_filepath("rna")

def dna_to_rna(sequence):
    rna_list = []
    for n in sequence:
        rna_list.append("U" if n == "T" else n)
    return "".join(rna_list)

with open(filepath, "r") as f:
    sequence = f.read().strip()

result = dna_to_rna(sequence)

pyperclip.copy(result)
print(result)