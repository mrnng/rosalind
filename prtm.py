# Calculating Protein Mass
# Problem link: https://rosalind.info/problems/prtm/

import utils
import pyperclip

filepath = utils.get_filepath("prtm")

def protein_mass(protein):
    result = 0
    for a in protein:
        result += utils.MONOISOTOPIC_MASS_TABLE[a]
    return result

with open(filepath, "r") as f:
    protein = f.read().strip()

result = round(protein_mass(protein), 3)

pyperclip.copy(result)
print(result)