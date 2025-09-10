# Introduction to Random Strings
# Problem link: https://rosalind.info/problems/prob/

import pyperclip
import math
from collections import Counter
from utils.io import get_filepath

filepath = get_filepath()

def solve(sequence, gc_content):
    result_list = []

    for p in gc_content:
        q = 1 - p
        probability = 1
        for b in sequence:
            probability *= p / 2 if b in "GC" else q / 2
        result_list.append(math.log(probability, 10))

    return " ".join(str(round(v, 3)) for v in result_list)

if __name__ == "__main__":
    data = filepath.read_text().split()
    sequence = data[0]
    gc_content = map(float, data[1::])

    result = solve(sequence, gc_content)
    pyperclip.copy(result)
    print(result)