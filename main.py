from itertools import chain,combinations,permutations
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint

API_KEY = '6N6NCHHOY72NXZ4T'
#
# cc = ForeignExchange(key=API_KEY)
#
# data,_ = cc.get_currency_exchange_rate(from_currency='EUR',to_currency='USD')
#
# # pprint(data)
# print(data['5. Exchange Rate'])

def perms(base_pairs):
    perms = []
    for i in range(1,len(base_pairs)+1):
        perms.append(list(permutations(base_pairs,i)))
    return perms


base_pairs = ['USD', 'EUR', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD', 'HKD']
base_perms = perms(base_pairs) # total amount of items in this dataset is 109600...
base_perms.pop(0)
# At this point, index 0 contains base pairs permutations of basepairs combination of 2 elements


cc = ForeignExchange(key=API_KEY)

data1,_ = cc.get_currency_exchange_rate(from_currency='EUR',to_currency='USD')
data2,_ = cc.get_currency_exchange_rate(from_currency='USD',to_currency='EUR')

print(str(data1['5. Exchange Rate'])+" - "+str(data2['5. Exchange Rate']))
