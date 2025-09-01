# Counting DNA Nucleotides
# Problem link: https://rosalind.info/problems/dna/

import utils
import pyperclip

filepath = utils.get_filepath("dna")

def count_nucleotides(sequence):
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    for n in sequence:
        count[n] += 1
    return f"{count['A']} {count['C']} {count['G']} {count['T']}"

with open(filepath, "r") as f:    
    sequence = f.read().strip()

result = count_nucleotides(sequence)

pyperclip.copy(result)
print(result)