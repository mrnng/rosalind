import sys
from pathlib import Path

def get_filepath():
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python3 -m "
            f"problems.{Path(sys.argv[0]).name[:-3]} <filepath>")
    path = Path(sys.argv[1])
    if not path.exists():
        raise SystemExit(f"Error, file not found: {path}")
    if not path.is_file():
        raise SystemExit(f"Error, {path} is not a file.")
    return path

# returns a dict of {id: sequence}
def parse_fasta(data: str) -> dict[str, str]:
    """
    Parse FASTA-formatted data from a string and return a dictionary
    mapping sequence IDs to sequences.
    """
    fasta_dict = {}
    id = ""
    sequence_parts = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue  # skip empty lines
        if line.startswith(">"):
            if id:
                fasta_dict[id] = "".join(sequence_parts)
            id = line[1:]
            sequence_parts = []
        else:
            sequence_parts.append(line)

    if id:
        fasta_dict[id] = "".join(sequence_parts)

    return fasta_dict
