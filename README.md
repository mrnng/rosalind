# Rosalind Solutions

This repository contains my solutions to Bioinformatics Stronghold problems
from the [Rosalind Project](rosalind.info/).

## Project Structure

Each problem is implemented in its own file, with a shared utils module
providing helper functions.

rosalind/
|--problems/ # individual problem solutions
|--utils/
|  |--io.py  # input/output helper functions
|  |--bio.py # bioinformatics constants

## Requirements

- Python 3.9+
- [pyperclip](https://pypi.org/project/pyperclip/) (for copying the output to
the clipboard)

I'm using pyperclip to make submitting solutions to the website easier.

## Usage

Clone the repository:

```bash
git clone https://github.com/mrnng/rosalind.git
```

Run a problem solution (always run from the root of the rosalind directory):
```bash
cd rosalind
python3 -m problems.problem_id path/to/input/file
```

For example, to run the solution for "Counting DNA Nucleotides" with an input
text file in the root directory:
```bash
python3 -m problems.dna input.txt
```

## Notes

The aim of this project is to learn bioinformatics through problem-solving.

As I work through it, I'm learning the required biology and developing a small
bioinformatics library.
