# Mendel's First Law
# Problem link: https://rosalind.info/problems/iprb/

import utils
import pyperclip
from math import comb

filepath = utils.get_filepath("iprb")

def iprb(k, m, n):
    total = k + m + n
    return (
        comb(k, 2) +
        k * m +
        k * n +
        comb(m, 2) * 0.75 +
        m * n * 0.5
    ) / comb(total, 2)

with open(filepath, "r") as f:
    content = f.read().strip()

k, m, n = map(int, content.split(" "))

result = iprb(k, m, n)

pyperclip.copy(result)
print(result)