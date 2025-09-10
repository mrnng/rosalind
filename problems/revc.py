# Complementing a Strand of DNA
# Problem link: https://rosalind.info/problems/revc/

import pyperclip
from utils.io import get_filepath
from utils.bio import DNA_COMPLEMENT_TABLE

filepath = get_filepath()

def solve(sequence):
    return "".join([DNA_COMPLEMENT_TABLE[n] for n in sequence])[::-1]

if __name__ == "__main__":
    sequence = filepath.read_text().strip()

    result = solve(sequence)

    pyperclip.copy(result)
    print(result)