# Computing GC Content
# Problem link: https://rosalind.info/problems/gc/

import pyperclip
from utils.io import get_filepath, parse_fasta

filepath = get_filepath()

def solve(fasta_dict):
    def gc_content(sequence):
        gc = sequence.count("G") + sequence.count("C")
        return gc / len(sequence) * 100

    gc_list = {seq_id: gc_content(seq) for seq_id, seq in fasta_dict.items()}
    max_id = max(gc_list, key=gc_list.get)

    return f"{max_id}\n{gc_list[max_id]}"

if __name__ == "__main__":
    data = filepath.read_text().strip()
    fasta_dict = parse_fasta(data)

    result = solve(fasta_dict)

    pyperclip.copy(result)
    print(result)