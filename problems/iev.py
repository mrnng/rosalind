# Calculating Expected Offspring
# Problem link: https://rosalind.info/problems/iev/

import pyperclip
from utils.io import get_filepath

filepath = get_filepath()

# Returns the expected value of dominant phenotype offspring given the number
# of couples in the form [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]
# In this case, each couple has 2 offspring
def solve(nums):
    # The probability of having an offspring with a dominant phenotype,
    # in the above order.
    offspring = 2
    probs = [1, 1, 1, 0.75, 0.5, 0]
    # Each couple has 'offspring' offspring and E(k*X) = k*E(X)
    return offspring * sum([x * y for x, y in zip(probs, nums)])

if __name__ == "__main__":
    nums = list(map(int, filepath.read_text().strip().split()))

    result = solve(nums)

    pyperclip.copy(result)
    print(result)