# Calculating Expected Offspring
# Problem link: https://rosalind.info/problems/iev/

import utils
import pyperclip

filepath = utils.get_filepath("iev")

# Returns the expected value of dominant phenotype offspring given the number
# of couples in the form [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]
def expected_dominant_phenotype(nums):
    # The probability of having an offspring with a dominant phenotype,
    # in the above order.
    probs = [1, 1, 1, 0.75, 0.5, 0]
    return sum([x * y for x, y in zip(probs, nums)])

with open(filepath, "r") as f:
    nums = list(map(int, f.read().strip().split()))

# Each couple has 2 offspring and E(2*X) = 2*E(X)
result = 2 * expected_dominant_phenotype(nums)

pyperclip.copy(result)
print(result)