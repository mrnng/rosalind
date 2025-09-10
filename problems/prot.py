# Translating RNA into Protein
# Problem link: https://rosalind.info/problems/prot/

import pyperclip
from utils.io import get_filepath
from utils.bio import CODON_TABLE

filepath = get_filepath()

def solve(sequence):
    prot_list = []
    for i in range(0, len(sequence), 3):
        sub = sequence[i:i+3]
        codon = CODON_TABLE[sub]
        if codon == "Stop":
            break
        else:
            prot_list.append(codon)
    return "".join(prot_list)

if __name__ == "__main__":
    sequence = filepath.read_text().strip()

    result = solve(sequence)

    pyperclip.copy(result)
    print(result)