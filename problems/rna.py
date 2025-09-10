# Transcribing DNA into RNA
# Problem link: https://rosalind.info/problems/rna/

import pyperclip
from utils.io import get_filepath

filepath = get_filepath()

def solve(sequence):
    return sequence.replace("T", "U")

if __name__ == "__main__":
    sequence = filepath.read_text().strip()

    result = solve(sequence)

    pyperclip.copy(result)
    print(result)