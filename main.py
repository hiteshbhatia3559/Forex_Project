from itertools import chain, combinations, permutations
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint

API_KEY = '6N6NCHHOY72NXZ4T'


def perms(base_pairs):
    perms = []
    for i in range(1, len(base_pairs) + 1):
        perms.append(list(permutations(base_pairs, i)))
    perms.pop(0)
    return perms


def chain_calculator(chain):
    chain = list(chain)
    i = 0
    net_PNL = float()
    while i < len(chain):
        if i != len(chain) - 1:
            data1, _ = cc.get_currency_exchange_rate(from_currency=chain[i], to_currency=chain[i + 1])
            data2, _ = cc.get_currency_exchange_rate(from_currency=chain[i + 1], to_currency=chain[i])
            first_number = round(float(data1['5. Exchange Rate']), 8)
            second_number = round(1 / float(data2['5. Exchange Rate']), 8)
            print(first_number / second_number)
        i += 1


base_pairs = ['USD', 'EUR', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD', 'HKD']
base_perms = perms(base_pairs)  # total amount of items in this dataset is 109600...
# At this point, index 0 contains base pairs permutations of basepairs combination of 2 elements
cc = ForeignExchange(key=API_KEY)

chain_calculator(base_perms[0][12])
