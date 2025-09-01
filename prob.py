# Introduction to Random Strings
# Problem link: https://rosalind.info/problems/prob/

import utils
import pyperclip
from collections import Counter
import math

filepath = utils.get_filepath("prob")

with open(filepath, "r") as f:
    input_list = f.read().split()
    sequence = input_list[0]
    gc_content_list = list(map(float, input_list[1:]))

result_list = []

for p in gc_content_list:
    q = 1 - p
    probability = 1
    for b in sequence:
        probability *= p/2 if b in "GC" else q/2
    result_list.append(math.log(probability, 10))

result = " ".join(str(round(v, 3)) for v in result_list)

pyperclip.copy(result)
print(result)