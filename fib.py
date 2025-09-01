# Rabbits and Recurrence Relations
# Problem link: https://rosalind.info/problems/fib/

import utils
import pyperclip

filepath = utils.get_filepath("fib")

def fib_k(n, k, cache={1:1, 2:1}):
    if n not in cache:
        cache[n] = fib_k(n-1, k, cache) + k * fib_k(n-2, k, cache)
    return cache[n]

with open(filepath, "r") as f:
    content = f.read().strip()

n, k = map(int, content.split(" "))

result = fib_k(n, k)

pyperclip.copy(result)
print(result)