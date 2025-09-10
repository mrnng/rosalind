# Mendel's First Law
# Problem link: https://rosalind.info/problems/iprb/

import pyperclip
from math import comb
from utils.io import get_filepath

filepath = get_filepath()

def solve(k, m, n):
    total = k + m + n
    return (
        comb(k, 2) +
        k * m +
        k * n +
        comb(m, 2) * 0.75 +
        m * n * 0.5
    ) / comb(total, 2)

if __name__ == "__main__":
    data = filepath.read_text().strip()
    k, m, n = map(int, data.split(" "))

    result = solve(k, m, n)

    pyperclip.copy(result)
    print(result)