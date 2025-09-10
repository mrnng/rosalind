# Finding a Motif in DNA
# Problem link: https://rosalind.info/problems/subs/

import pyperclip
from utils.io import get_filepath

filepath = get_filepath()

# t is the potential substring of s
def solve(s, t):
    indices = []
    for i, n in enumerate(s):
        if s[i:i+len(t)] == t:
            indices.append(i+1)
    return " ".join(map(str, indices))

if __name__ == "__main__":
    s, t = filepath.read_text().strip().split()

    result = solve(s, t)

    pyperclip.copy(result)
    print(result)