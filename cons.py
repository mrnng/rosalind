# Consensus and Profile
# Problem link: https://rosalind.info/problems/cons/

import utils
import pyperclip

filepath = utils.get_filepath("cons")
fasta_dict = utils.parse_fasta(filepath)

def consensus_and_profile(fasta_dict):
    sequences = list(fasta_dict.values())
    n = len(sequences[0])
    consensus = {k: [0 for _ in range(n)] for k in "ACGT"}
    for sequence in sequences:
        for i, b in enumerate(sequence):
            consensus[b][i] += 1
    profile = []
    for i in range(n):
        max_base = ""
        max_count = 0
        for b in "ACGT":
            if consensus[b][i] > max_count:
                max_base = b
                max_count = consensus[b][i]
        profile.append(max_base)
    profile_string = "".join(profile)
    consensus_string = "\n".join(
        f"{k}: " + " ".join(str(c) for c in v)
        for k, v in consensus.items()
    )
    return profile_string + "\n" + consensus_string

result = consensus_and_profile(fasta_dict)

pyperclip.copy(result)
print(result)