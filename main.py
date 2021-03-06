from itertools import chain, combinations, permutations

API_KEY = '6N6NCHHOY72NXZ4T'


def perms(base_pairs):
    perms = []
    for i in range(1, len(base_pairs) + 1):
        perms.append(list(permutations(base_pairs, i)))
    perms.pop(0)
    return perms


def chain_calculator(tuple_chain, matrix):
    chain = list(tuple_chain)
    base_pairs = ['USD', 'EUR', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD', 'HKD']
    # comb_base_pairs = combinations(base_pairs, 2)
    i, j, a, b, k = 0, 0, 0, 0, 0
    pnl = 1
    # Calculate list pnl
    for item in chain:
        if chain.index(item) == len(chain) - 1:
            pnl *= round(1 / round(matrix[base_pairs.index(chain[-2])][base_pairs.index(chain[-1])], 8), 8)
            break
        else:
            x = base_pairs.index(item)
            index_of_x_in_chain = chain.index(item)
            y = base_pairs.index(chain[index_of_x_in_chain + 1])
            pnl *= matrix[x][y]
    # Result return to caller
    string = '-'.join(chain) + '-' + chain[0]
    return {string: pnl}

if __name__ == "__main__":
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
    results = []
    f = open('results.csv', 'w+')
    for chains in base_perms:
        for chain in chains:
            result = chain_calculator(chain, matrix)
            if (list(result.keys())[0] < 0.99) and (list(result.keys())[0] > 0.95):
                results.append(results)
                f.write(str(list(result.keys())[0]))
                f.write(',')
                f.write(str(list(result.values())[0]))
                f.write('\n')

    f.close()
    print("All done, results in results.csv")
