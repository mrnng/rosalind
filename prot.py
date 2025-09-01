# Translating RNA into Protein
# Problem link: https://rosalind.info/problems/prot/

import utils
import pyperclip

filepath = utils.get_filepath("prot")

def rna_to_protein(sequence):
    prot_list = []
    for i in range(0, len(sequence), 3):
        sub = sequence[i:i+3]
        codon = utils.CODON_TABLE[sub]
        if codon == "Stop":
            break
        else:
            prot_list.append(codon)
    return "".join(prot_list)

with open(filepath, "r") as f:
    sequence = f.read().strip()

result = rna_to_protein(sequence)

pyperclip.copy(result)
print(result)