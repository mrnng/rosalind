import sys

#  CONSTANTS
# -----------

CODON_TABLE = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
}

DNA_COMPLEMENT_TABLE = {
    "A": "T",
    "C": "G",
    "G": "C",
    "T": "A"
}

MONOISOTOPIC_MASS_TABLE = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333
}

#  FUNCTIONS
# -----------

def get_filepath(program_name):
    if len(sys.argv) < 2:
        raise SystemExit(f"Usage: {program_name}.py <filepath>")
    return sys.argv[1]

# returns a dict of {id: sequence}
def parse_fasta(filepath):
    fasta_dict = {}
    with open(filepath, "r") as f:
        id = ""
        sequence_parts = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if id != "":
                    fasta_dict[id] = "".join(sequence_parts)
                id = line[1::]
                sequence_parts = []
            else:
                sequence_parts.append(line)
        if id != "":
            fasta_dict[id] = "".join(sequence_parts)
    return fasta_dict
