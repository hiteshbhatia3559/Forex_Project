from itertools import chain, combinations, permutations

API_KEY = '6N6NCHHOY72NXZ4T'


def perms(base_pairs):
    perms = []
    for i in range(1, len(base_pairs) + 1):
        perms.append(list(permutations(base_pairs, i)))
    perms.pop(0)
    return perms


def chain_calculator(tuple_chain, matrix):
    chain_names = list(tuple_chain)
    chain = correlation(chain_names,matrix)
    pnl = 1
    i, j = 0, 0
    while i < len(chain):
        if i == 0:
            pnl = chain[i] * chain[i + 1]
            i += 1
        else:
            if i == len(chain) - 1:
                pnl *= chain[0]
                break
            else:
                pnl *= chain[i+1]
                i += 1

def correlation()


base_pairs = ['USD', 'EUR', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD', 'HKD']
matrix = [
    (1, 1.1326, 0.009, 1.329, 0.9974, 0.7499, 0.7085, 0.1274),
    (0.8829, 1, 0.0079, 1.1734, 0.8811, 0.6621, 0.6256, 0.1125),
    (111.48, 126.2622, 1, 148.1569, 111.2464, 83.5933, 78.9836, 14.2015),
    (0.7524, 0.8522, 0.0068, 1, 0.7509, 0.5642, 0.5331, 0.0959),
    (1.0021, 1.135, 0.009, 1.3318, 1, 0.7514, 0.71, 0.1277),
    (1.3336, 1.5104, 0.0116, 1.7724, 1.3308, 1, 0.9449, 0.1699),
    (1.4114, 1.5986, 0.012, 1.8758, 1.4085, 1.0584, 1, 0.1798),
    (7.8499, 8.8908, 0.0704, 10.4325, 7.8334, 5.8862, 5.5617, 1)
]
base_perms = perms(base_pairs)  # total amount of items in this dataset is 109600...
# At this point, index 0 contains base pairs permutations of basepairs combination of 2 elements
result = []
for chains in base_perms:
    for chain in chains:
        result.append(chain_calculator(chain, matrix))
