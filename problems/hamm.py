# Counting Point Mutations
# Problem link: https://rosalind.info/problems/hamm/

import pyperclip
from utils.io import get_filepath

filepath = get_filepath()

def solve(seq_1, seq_2):
    result = 0
    for i, j in zip(seq_1, seq_2):
        if i != j:
            result += 1

    return result

if __name__ == "__main__":
    seq_1, seq_2 = filepath.read_text().strip().split()

    result = solve(seq_1, seq_2)

    pyperclip.copy(result)
    print(result)