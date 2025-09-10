# Counting DNA Nucleotides
# Problem link: https://rosalind.info/problems/dna/

import pyperclip
from collections import Counter
from utils.io import get_filepath

filepath = get_filepath()

def solve(sequence):
    count = Counter(sequence)
    return f"{count['A']} {count['C']} {count['G']} {count['T']}"

if __name__ == "__main__":  
    sequence = filepath.read_text().strip()

    result = solve(sequence)

    pyperclip.copy(result)
    print(result)