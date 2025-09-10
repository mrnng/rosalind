# Rabbits and Recurrence Relations
# Problem link: https://rosalind.info/problems/fib/

import pyperclip
from utils.io import get_filepath

filepath = get_filepath()

def solve(n, k, cache={1:1, 2:1}):
    if n not in cache:
        cache[n] = solve(n - 1, k, cache) + k * solve(n - 2, k, cache)
    return cache[n]

if __name__ == "__main__":
    data = filepath.read_text().strip()
    n, k = map(int, data.split(" "))

    result = solve(n, k)

    pyperclip.copy(result)
    print(result)