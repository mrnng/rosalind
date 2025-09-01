# Finding a Motif in DNA
# Problem link: https://rosalind.info/problems/subs/

import utils
import pyperclip

filepath = utils.get_filepath("subs")

# t is the potential substring of s
def substring_positions(s, t):
    indices = []
    for i, n in enumerate(s):
        if s[i:i+len(t)] == t:
            indices.append(i+1)
    return indices

with open(filepath, "r") as f:
    sequences = []
    for line in f:
        sequences.append(line.strip())

s, t = sequences

result = " ".join(map(str, substring_positions(s, t)))

pyperclip.copy(result)
print(result)