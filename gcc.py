# Computing GC Content
# Problem link: https://rosalind.info/problems/gc/

import utils
import pyperclip

filepath = utils.get_filepath("gcc")
fasta_dict = utils.parse_fasta(filepath)

def gc_content(sequence):
    total = 0
    for n in sequence:
        if n in "GC":
            total += 1
    return total / len(sequence) * 100

gc_list = {key: gc_content(value) for key, value in fasta_dict.items()}

max_key = max(gc_list, key=gc_list.get)

result = f"""{max_key}
{gc_list[max_key]}"""

pyperclip.copy(result)
print(result)