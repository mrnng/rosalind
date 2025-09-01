# Complementing a Strand of DNA
# Problem link: https://rosalind.info/problems/revc/

import utils
import pyperclip

filepath = utils.get_filepath("revc")

def reverse_complement(sequence):
    complement_list = []
    for n in sequence:
        complement_list.append(utils.DNA_COMPLEMENT_TABLE[n])
    return complement_list[::-1]

with open(filepath, "r") as f:
    sequence = f.read().strip()

result = reverse_complement(sequence)

pyperclip.copy(result)
print(result)