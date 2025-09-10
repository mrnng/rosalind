# Calculating Protein Mass
# Problem link: https://rosalind.info/problems/prtm/

import pyperclip
from utils.io import get_filepath
from utils.bio import MONOISOTOPIC_MASS_TABLE

filepath = get_filepath()

def solve(protein):
    return sum([MONOISOTOPIC_MASS_TABLE[a] for a in protein])

if __name__ == "__main__":
    protein = filepath.read_text().strip()

    result = solve(protein)

    pyperclip.copy(result)
    print(result)