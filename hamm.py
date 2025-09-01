# Counting Point Mutations
# Problem link: https://rosalind.info/problems/hamm/

import utils
import pyperclip

filepath = utils.get_filepath("hamm")

def hamming_distance(seq_1, seq_2):
    result = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            result += 1

with open(filepath, "r") as f:
    sequences = [line for line in f]

seq_1, seq_2 = sequences

result = hamming_distance(seq_1, seq_2)

pyperclip.copy(result)
print(result)