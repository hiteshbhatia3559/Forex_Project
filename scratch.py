from itertools import combinations

base_pairs = ['USD', 'EUR', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD', 'HKD']

new = list(combinations(base_pairs,2))

print(new)
